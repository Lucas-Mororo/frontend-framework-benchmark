const lighthouseModule = require('lighthouse');
const chromeLauncher = require('chrome-launcher');
const fs = require('fs');
const waitPort = require('wait-port');

// Ajuste para acessar a função padrão do módulo lighthouse
const lighthouse = lighthouseModule.default || lighthouseModule;

const urls = [
    'http://nginx-react:80/',
    'http://nginx-vue:80/',
    'http://nginx-angular:80/'
];

async function waitForService(url) {
    const [host, port] = url.replace('http://', '').split(':');
    console.log("🚀 ~ waitForService ~ port:", port)
    console.log("🚀 ~ waitForService ~ host:", host)
    await waitPort({ host, port: parseInt(port, 10), timeout: 30000, interval: 1000 });
    console.log(`Service at ${url} is ready`);
}

async function runLighthouse(url, framework) {
    let chrome;
    try {
        chrome = await chromeLauncher.launch({
            chromeFlags: [
                '--headless',
                '--no-sandbox',
                '--disable-gpu',
                '--disable-dev-shm-usage'
            ],
            chromePath: process.env.CHROME_PATH || '/usr/bin/chromium',
            logLevel: 'verbose'
        });
        console.log(`🚀 ~ runLighthouse ~ chrome launched on port: ${chrome.port}`);
    } catch (error) {
        console.error('🚀 ~ Failed to launch Chrome:', error);
        throw error;
    }

    const options = { output: ['json', 'html'], port: chrome.port };
    console.log("🚀 ~ runLighthouse ~ options:", options)

    for (let i = 1; i <= 3; i++) {
        try {
            const runnerResult = await lighthouse(url, options);
            const reportJson = runnerResult.report[0];
            const reportHtml = runnerResult.report[1];
            fs.writeFileSync(`/results/${framework}-run-${i}.json`, reportJson);
            fs.writeFileSync(`/results/${framework}-run-${i}.html`, reportHtml);
            console.log(`Completed run ${i} for ${framework}`);
        } catch (error) {
            console.error(`Error during run ${i} for ${framework}:`, error);
        }
    }

    await chrome.kill();
}

async function main() {
    for (const url of urls) {
        const framework = url.split('/')[2];
        console.log(`Starting tests for ${framework}`);
        await waitForService(url);
        await runLighthouse(url, framework);
    }
}

main().catch(console.error);