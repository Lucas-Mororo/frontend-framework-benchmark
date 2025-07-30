/**
 * Lighthouse Performance Testing Script
 * 
 * This script performs automated performance testing using Google Lighthouse
 * on multiple web applications (React, Vue, Angular) running in Docker containers.
 * Results are organized by framework in separate directories.
 */

const lighthouseModule = require('lighthouse');
const chromeLauncher = require('chrome-launcher');
const fs = require('fs');
const path = require('path');
const waitPort = require('wait-port');

// Handle different module export formats
const lighthouse = lighthouseModule.default || lighthouseModule;

// Service URLs for testing (Docker service names)
const urls = ['http://nginx-react:80/', 'http://nginx-vue:80/', 'http://nginx-angular:80/'];

const resultsBaseDir = '/results';

/**
 * Wait for a service to become available on the specified URL
 * @param {string} url - Target service URL
 */
async function waitForService(url) {
    const urlWithoutProtocol = url.replace('http://', '').replace(/\/$/, '');
    const [host, portWithSlash] = urlWithoutProtocol.split(':');
    const port = portWithSlash || '80';

    await waitPort({
        host,
        port: parseInt(port, 10),
        timeout: 30000,
        interval: 1000
    });

    console.log(`✅ Service ready: ${url}`);
}

/**
 * Create directory if it doesn't exist
 * @param {string} dirPath - Directory path to create
 */
function ensureDirectoryExists(dirPath) {
    if (!fs.existsSync(dirPath)) {
        fs.mkdirSync(dirPath, { recursive: true });
        console.log(`📁 Created directory: ${dirPath}`);
    }
}

/**
 * Execute Lighthouse performance tests
 * @param {string} url - URL to test
 * @param {string} framework - Framework name for file organization
 */
async function runLighthouse(url, framework) {
    let chrome;

    try {
        // Launch Chrome instance with headless configuration
        chrome = await chromeLauncher.launch({
            chromeFlags: [
                '--headless',
                '--no-sandbox',
                '--disable-gpu',
                '--disable-dev-shm-usage'
            ],
            chromePath: process.env.CHROME_PATH || '/usr/bin/chromium'
        });

    } catch (error) {
        console.error(`❌ Failed to launch Chrome for ${framework}:`, error);
        throw error;
    }

    const options = {
        output: ['json', 'html'],
        port: chrome.port
    };

    // Create framework-specific directory
    const frameworkDir = path.join(resultsBaseDir, framework);
    ensureDirectoryExists(frameworkDir);

    // Run 3 consecutive tests for statistical consistency
    for (let i = 1; i <= 100; i++) {
        try {
            console.log(`📊 Running test ${i}/100 for ${framework}...`);

            const runnerResult = await lighthouse(url, options);
            const reportJson = runnerResult.report[0];
            const reportHtml = runnerResult.report[1];

            // Save reports to framework-specific directory
            const jsonFilePath = path.join(frameworkDir, `${framework}-run-${i}.json`);
            const htmlFilePath = path.join(frameworkDir, `${framework}-run-${i}.html`);

            fs.writeFileSync(jsonFilePath, reportJson);
            fs.writeFileSync(htmlFilePath, reportHtml);

            console.log(`✅ Test ${i} completed for ${framework}`);

        } catch (error) {
            console.error(`❌ Test ${i} failed for ${framework}:`, error);
        }
    }

    await chrome.kill();
}

/**
 * Main execution function
 */
async function main() {
    console.log('🚀 Starting Lighthouse performance analysis...');

    ensureDirectoryExists(resultsBaseDir);

    for (const url of urls) {
        // Extract framework name from Docker service name
        const serviceName = url.replace('http://', '').split(':')[0];
        const framework = serviceName.replace('nginx-', '');

        console.log(`\n🎯 Testing ${framework.toUpperCase()} application`);

        try {
            await waitForService(url);
            await runLighthouse(url, framework);
            console.log(`✅ ${framework.toUpperCase()} testing completed\n`);

        } catch (error) {
            console.error(`❌ ${framework.toUpperCase()} testing failed:`, error);
        }
    }

    console.log('🎉 All performance tests completed!');
}

// Execute main function with error handling
main().catch((error) => {
    console.error('💥 Fatal error:', error);
    process.exit(1);
});