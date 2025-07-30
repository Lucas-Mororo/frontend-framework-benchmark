# Proposta de Infraestrutura com Código para Benchmarks de Frameworks Web Frontend JavaScript

Bem-vindo ao repositório do meu Trabalho de Conclusão de Curso (TCC), intitulado **"Proposta de Infraestrutura com Código para Benchmarks de Frameworks Web Frontend JavaScript"**. Este projeto foi desenvolvido com o objetivo principal de realizar uma análise comparativa detalhada entre três dos frameworks JavaScript mais populares e amplamente utilizados no desenvolvimento de interfaces web modernas: **ReactJS**, **Angular** e **Vue.js**. Para isso, implementei uma aplicação prática do tipo "to-do list" (lista de tarefas) em cada um desses frameworks, utilizando uma infraestrutura moderna baseada em contêineres Docker e ferramentas de benchmark como o Lighthouse, mantidas pelo Google.

O propósito deste trabalho é ir além de uma simples comparação superficial, oferecendo uma metodologia estruturada e replicável que permita avaliar o desempenho, a facilidade de uso e a eficiência desses frameworks em um cenário prático. A infraestrutura foi projetada para ser portátil, consistente e escalável, utilizando tecnologias como Docker, Nginx e Vite, enquanto o gerenciamento de estado foi padronizado com o **Redux Toolkit** em todas as aplicações, garantindo uma base comum para a análise. Este TCC busca fornecer insights valiosos para desenvolvedores, arquitetos de software e empresas que enfrentam o desafio de escolher a tecnologia mais adequada para seus projetos de desenvolvimento web, considerando tanto aspectos técnicos quanto práticos.

A data atual é **28 de março de 2025**, e este projeto reflete o estado da arte das tecnologias frontend disponíveis até este momento, com atualizações contínuas no conhecimento das ferramentas utilizadas.

---

## Contexto e Motivação

O desenvolvimento web frontend passou por uma transformação significativa na última década, impulsionada pelo aumento da complexidade das aplicações web e pela demanda por interfaces de usuário rápidas, interativas e responsivas. Frameworks como ReactJS, Angular e Vue.js emergiram como líderes nesse cenário, cada um com suas próprias filosofias, abordagens e comunidades de suporte. O ReactJS, criado pelo Facebook, é conhecido por sua flexibilidade e ecossistema rico de bibliotecas; o Angular, mantido pelo Google, oferece uma solução completa e robusta para aplicações corporativas; e o Vue.js, desenvolvido por Evan You, destaca-se por sua simplicidade e curva de aprendizado suave.

Apesar de sua popularidade, a escolha entre esses frameworks não é trivial. Fatores como desempenho em diferentes condições de carga, facilidade de implementação para equipes com variados níveis de experiência, e eficiência no uso de recursos computacionais são cruciais, mas frequentemente difíceis de mensurar sem uma análise prática e controlada. Muitas vezes, as decisões são baseadas em preferências pessoais, documentação disponível ou tendências de mercado, em vez de dados objetivos.

Este TCC foi motivado pela necessidade de preencher essa lacuna, criando uma abordagem sistemática para comparar esses frameworks em um ambiente padronizado. A ideia central é utilizar uma infraestrutura como código (IaC) para garantir que os testes sejam consistentes e replicáveis, eliminando variáveis externas como configurações locais ou diferenças de hardware. Além disso, a escolha de uma aplicação simples como uma "to-do list" permite focar nas características intrínsecas de cada framework, enquanto a integração de ferramentas modernas como Docker, Nginx e Lighthouse assegura que os resultados sejam relevantes para o desenvolvimento web contemporâneo. O objetivo final é oferecer uma base sólida para que desenvolvedores e empresas possam tomar decisões informadas, respaldadas por métricas concretas e uma metodologia bem definida.

---

## Objetivos do Projeto

O projeto foi estruturado com os seguintes objetivos específicos, cada um contribuindo para a realização da proposta geral:

1. **Comparação de Frameworks**: Avaliar de forma detalhada o desempenho (tempo de carregamento, capacidade de resposta, uso de recursos), a facilidade de uso (curva de aprendizado, clareza da API, produtividade no desenvolvimento) e a eficiência (escalabilidade, tamanho do bundle gerado) dos frameworks ReactJS, Angular e Vue.js em um cenário prático de desenvolvimento frontend, utilizando uma aplicação "to-do list" como base comum.
2. **Infraestrutura Moderna**: Desenvolver e implementar uma infraestrutura como código (IaC) utilizando Docker para criar ambientes isolados e consistentes, e Nginx como servidor web e proxy reverso, garantindo que os testes sejam portáteis e possam ser executados em diferentes máquinas ou sistemas operacionais sem perda de fidelidade nos resultados.
3. **Benchmarks Realistas**: Utilizar a ferramenta Lighthouse para coletar métricas detalhadas de desempenho, acessibilidade, boas práticas de desenvolvimento e SEO, simulando condições reais de uso e permitindo uma análise quantitativa e qualitativa dos frameworks em um ambiente controlado.
4. **Documentação e Replicabilidade**: Produzir uma solução bem documentada, com instruções claras e arquivos de configuração (como Docker Compose) que permitam a outros pesquisadores, estudantes ou profissionais replicar o estudo ou adaptá-lo para diferentes frameworks ou cenários, promovendo a continuidade e expansão do trabalho.

Esses objetivos foram definidos para atender tanto às exigências acadêmicas do TCC quanto às necessidades práticas do mercado de desenvolvimento web.

---

## Tecnologias Utilizadas

A escolha das tecnologias foi cuidadosamente planejada para refletir as melhores práticas do desenvolvimento web moderno e atender aos objetivos do projeto. Abaixo está uma descrição detalhada de cada tecnologia utilizada, incluindo seu propósito e como foi aplicada no contexto do TCC:

### Frameworks Frontend
- **ReactJS**: Uma biblioteca JavaScript de código aberto criada pelo Facebook, amplamente utilizada para construir interfaces de usuário baseadas em componentes reutilizáveis. Neste projeto, o React foi combinado com o **Redux Toolkit** para gerenciamento de estado e o **React-Redux** para conectar o estado global aos componentes, garantindo uma arquitetura previsível e escalável. A versão utilizada foi a 19.0.0, refletindo as atualizações mais recentes até março de 2025.
- **Angular**: Um framework completo mantido pelo Google, projetado para aplicações web robustas e corporativas. Ele oferece suporte nativo a TypeScript, injeção de dependências e uma CLI poderosa para automação de tarefas. No TCC, o Angular (versão 19.2.4) foi integrado ao **Redux Toolkit** para gerenciamento de estado, uma abordagem menos comum, mas adotada aqui para padronização com os outros frameworks.
- **Vue.js**: Um framework progressivo criado por Evan You, conhecido por sua simplicidade e desempenho em aplicações de pequeno a médio porte. A versão 3.5.13 foi utilizada, com o **Redux Toolkit** substituindo o Vuex (embora este esteja presente como dependência) para manter a consistência no gerenciamento de estado entre os três frameworks.

### Ferramentas de Desenvolvimento
- **TypeScript**: Uma extensão do JavaScript que adiciona tipagem estática, utilizada em todos os projetos para aumentar a robustez do código, facilitar a detecção precoce de erros e melhorar a manutenibilidade. A versão 5.7.2 (ou 5.8.2 no Angular) foi adotada, aproveitando recursos como tipos genéricos e inferência avançada.
- **Tailwind CSS**: Um framework CSS utilitário que permite criar interfaces responsivas e personalizadas de forma rápida, utilizando classes pré-definidas em vez de escrever estilos tradicionais extensos. A versão 4.0.15 (ou 4.0.17 no Angular) foi integrada via PostCSS ou Vite, reduzindo o tempo de estilização e garantindo consistência visual entre as aplicações.
- **Vite**: Uma ferramenta de build moderna que utiliza ES Modules nativos e compilação sob demanda, oferecendo inicialização rápida e recarga automática (hot-reload) durante o desenvolvimento. Foi usada nas aplicações React e Vue (versão 6.2.0), enquanto o Angular utilizou o Angular CLI devido à sua integração nativa com o framework.
- **Redux Toolkit**: Uma biblioteca oficial do Redux que simplifica o gerenciamento de estado com padrões como "slices", reducers imutáveis e integração com middlewares. A versão 2.6.1 foi utilizada em todos os três frameworks, garantindo uma abordagem estruturada e previsível para o estado da "to-do list" (ex.: adicionar, remover e listar tarefas).

### Infraestrutura
- **Docker**: Uma plataforma open-source de contêineres que encapsula dependências, configurações e código em ambientes isolados. Foi utilizado para criar contêineres para cada aplicação (React, Vue, Angular), o Nginx e o Lighthouse, assegurando que os testes fossem executados em condições idênticas, independentemente do sistema hospedeiro.
- **Nginx**: Um servidor web de alta performance e código aberto, configurado como proxy reverso para direcionar requisições às instâncias das aplicações. Também suporta balanceamento de carga e cache, otimizando o tráfego de rede durante os benchmarks. A versão mais recente (`latest`) foi usada nos contêineres.
- **Docker Compose**: Uma ferramenta para definir e gerenciar aplicações multi-contêineres, utilizada para orquestrar os serviços do projeto. Três arquivos foram criados: um para desenvolvimento (`docker-compose-dev.yml`), um para build (`docker-compose-build.yml`) e um para produção/teste (`docker-compose.yml`).

### Análise de Desempenho
- **Lighthouse**: Uma ferramenta automatizada de código aberto mantida pelo Google, integrada ao projeto via Docker. Ela analisa páginas web com base em métricas como desempenho (ex.: FCP, LCP), acessibilidade, boas práticas e SEO, gerando relatórios detalhados em formato JSON que serviram como base para os benchmarks.

---

## Estrutura do Projeto

A estrutura de pastas foi projetada para organizar de forma clara as aplicações dos frameworks, os serviços de infraestrutura e os resultados dos benchmarks. Aqui está uma visão detalhada:

```
TCC/
├── benchmark-frameworks/
│   ├── angular-app/              # Diretório da aplicação Angular
│   │   ├── .angular/             # Arquivos de configuração gerados pelo Angular CLI
│   │   ├── .vscode/              # Configurações específicas para o Visual Studio Code
│   │   ├── dist/                 # Artefatos gerados pelo comando `ng build`
│   │   ├── node_modules/         # Dependências instaladas via npm
│   │   ├── public/               # Arquivos estáticos públicos (ex.: favicon, index.html)
│   │   └── src/                  # Código-fonte da aplicação (componentes, serviços, etc.)
│   ├── lighthouse/               # Configurações e scripts para execução do Lighthouse
│   ├── nginx/                    # Arquivos de configuração do Nginx (ex.: nginx.conf)
│   ├── react-app/                # Diretório da aplicação React
│   │   ├── dist/                 # Artefatos gerados pelo comando `vite build`
│   │   ├── node_modules/         # Dependências instaladas via npm
│   │   ├── public/               # Arquivos estáticos públicos
│   │   └── src/                  # Código-fonte da aplicação (componentes, Redux slices)
│   ├── results/                  # Relatórios gerados pelo Lighthouse (ex.: JSON, HTML)
│   └── vue-app/                  # Diretório da aplicação Vue.js
│       ├── .vscode/              # Configurações para o Visual Studio Code
│       ├── dist/                 # Artefatos gerados pelo comando `vite build`
│       ├── node_modules/         # Dependências instaladas via npm
│       ├── public/               # Arquivos estáticos públicos
│       └── src/                  # Código-fonte da aplicação (componentes, Redux slices)
├── docker-compose.yml            # Configuração para ambiente de produção/teste
├── docker-compose-dev.yml        # Configuração para ambiente de desenvolvimento
└── docker-compose-build.yml      # Configuração para build das aplicações
```

- **`angular-app`, `react-app`, `vue-app`**: Contêm o código-fonte, dependências e artefatos de build de cada aplicação "to-do list". Cada pasta segue a estrutura padrão do respectivo framework, com ajustes para integrar TypeScript, Tailwind CSS e Redux Toolkit.
- **`lighthouse`**: Inclui os arquivos necessários para configurar e executar os benchmarks, como o Dockerfile e scripts de automação.
- **`nginx`**: Armazena as configurações do servidor Nginx, como o arquivo `nginx.conf`, que define o proxy reverso e o mapeamento de portas.
- **`results`**: Diretório onde os relatórios do Lighthouse são salvos após a execução dos benchmarks, geralmente em formato JSON ou HTML.

---

## Dependências dos Projetos

Abaixo estão os arquivos `package.json` completos de cada aplicação, detalhando as dependências de produção e desenvolvimento, com ênfase no uso do **Redux Toolkit** como solução de gerenciamento de estado em todos os projetos:

### `angular-app/package.json`
```json
{
  "name": "todo-list-angular",
  "version": "0.0.0",
  "scripts": {
    "ng": "ng",
    "start": "ng serve --port 3000",
    "build": "ng build",
    "watch": "ng build --watch --configuration development",
    "test": "ng test"
  },
  "private": true,
  "dependencies": {
    "@angular/common": "^19.2.4",
    "@angular/compiler": "^19.2.4",
    "@angular/core": "^19.2.4",
    "@angular/forms": "^19.2.4",
    "@angular/platform-browser": "^19.2.4",
    "@angular/platform-browser-dynamic": "^19.2.4",
    "@angular/router": "^19.2.4",
    "@reduxjs/toolkit": "^2.6.1",
    "@tailwindcss/postcss": "^4.0.15",
    "postcss": "^8.5.3",
    "rxjs": "^7.8.2",
    "tailwindcss": "^4.0.17",
    "tslib": "^2.8.1",
    "zone.js": "^0.15.0"
  },
  "devDependencies": {
    "@angular-devkit/build-angular": "^19.2.5",
    "@angular/cli": "^19.2.5",
    "@angular/compiler-cli": "^19.2.4",
    "@types/jasmine": "^5.1.7",
    "jasmine-core": "^5.6.0",
    "karma": "^6.4.4",
    "karma-chrome-launcher": "^3.2.0",
    "karma-coverage": "^2.2.1",
    "karma-jasmine": "^5.1.0",
    "karma-jasmine-html-reporter": "^2.1.0",
    "typescript": "^5.8.2"
  }
}
```

### `react-app/package.json`
```json
{
  "homepage": "/react",
  "name": "todo-list",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite --port 3000",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "@reduxjs/toolkit": "^2.6.1",
    "@tailwindcss/postcss": "^4.0.15",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "react-redux": "^9.2.0"
  },
  "devDependencies": {
    "@eslint/js": "^9.21.0",
    "@types/react": "^19.0.10",
    "@types/react-dom": "^19.0.4",
    "@vitejs/plugin-react": "^4.3.4",
    "autoprefixer": "^10.4.21",
    "eslint": "^9.21.0",
    "eslint-plugin-react-hooks": "^5.1.0",
    "eslint-plugin-react-refresh": "^0.4.19",
    "globals": "^15.15.0",
    "postcss": "^8.5.3",
    "tailwindcss": "^4.0.15",
    "typescript": "~5.7.2",
    "typescript-eslint": "^8.24.1",
    "vite": "^6.2.0"
  }
}
```

### `vue-app/package.json`
```json
{
  "name": "todo-list-vue",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite --port 3000",
    "build": "vue-tsc -b && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@reduxjs/toolkit": "^2.6.1",
    "@tailwindcss/vite": "^4.0.15",
    "tailwindcss": "^4.0.15",
    "vue": "^3.5.13",
    "vuex": "^4.1.0"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^5.2.1",
    "@vue/tsconfig": "^0.7.0",
    "typescript": "~5.7.2",
    "vite": "^6.2.0",
    "vue-tsc": "^2.2.4"
  }
}
```

**Nota Importante**: Embora o `vuex` esteja listado como dependência no projeto Vue, o **Redux Toolkit** foi utilizado como a solução principal de gerenciamento de estado em todas as aplicações, garantindo consistência na implementação da lógica de estado (ex.: tarefas da "to-do list"). Isso foi uma decisão deliberada para facilitar a comparação direta entre os frameworks, eliminando variações decorrentes de diferentes bibliotecas de estado.

---

## Configuração com Docker Compose

O projeto utiliza três arquivos `docker-compose` distintos, cada um com um propósito específico no ciclo de vida do desenvolvimento e teste das aplicações:

### 1. `docker-compose.yml` (Ambiente de Produção/Teste)
Este arquivo define os serviços necessários para executar as aplicações em um ambiente de teste e realizar os benchmarks com o Lighthouse:
- **nginx-react**: Contêiner Nginx que serve a aplicação React na porta `8080`, mapeando o diretório `react-app/dist` para o servidor web.
- **nginx-vue**: Contêiner Nginx que serve a aplicação Vue na porta `8081`, mapeando `vue-app/dist`.
- **nginx-angular**: Contêiner Nginx que serve a aplicação Angular na porta `8082`, mapeando `angular-app/dist/todo-list-angular/browser`.
- **lighthouse**: Contêiner que executa os benchmarks, dependendo da saúde dos serviços Nginx (verificada via healthcheck com `curl`).
- **Rede**: `benchmark-net` (driver bridge), permitindo comunicação entre os serviços.

Cada serviço Nginx inclui um healthcheck para garantir que a aplicação esteja acessível antes da execução dos benchmarks.

### 2. `docker-compose-dev.yml` (Ambiente de Desenvolvimento)
Este arquivo configura um ambiente de desenvolvimento com recarga automática (hot-reload) para facilitar a codificação e testes locais:
- **react-dev**: Contêiner Node.js (versão 22.14-alpine) que roda a aplicação React na porta `3000`, com o comando `npm install && npm run dev`.
- **vue-dev**: Contêiner Node.js que roda a aplicação Vue na porta `3001`, com o mesmo comando.
- **angular-dev**: Contêiner Node.js que roda a aplicação Angular na porta `3002`, com ajustes no comando (`npm run start`) para suportar polling e desativar verificação de host.
- **Rede**: `dev-net` (driver bridge), isolando o ambiente de desenvolvimento.

Variáveis de ambiente como `CHOKIDAR_USEPOLLING` foram adicionadas para garantir a detecção de mudanças em sistemas de arquivos montados via Docker.

### 3. `docker-compose-build.yml` (Build das Aplicações)
Este arquivo é responsável por construir os artefatos finais das aplicações, gerando os arquivos otimizados para produção:
- **angular**: Contêiner Node.js que executa `npm install && npm run build` no diretório `angular-app`.
- **react**: Contêiner Node.js que executa `npm install && npm run build` no diretório `react-app`.
- **vue**: Contêiner Node.js que executa `npm install && npm run build` no diretório `vue-app`.

Os artefatos são salvos nos respectivos diretórios `dist` de cada aplicação, prontos para serem servidos pelo Nginx no ambiente de teste.

---

## Como Executar o Projeto

### Pré-requisitos
Antes de executar o projeto, certifique-se de que os seguintes softwares estejam instalados e configurados corretamente:
- **Docker**: Versão 20.10 ou superior, necessário para criar e gerenciar os contêineres.
- **Docker Compose**: Versão 1.29 ou superior, essencial para orquestrar os serviços multi-contêineres.
- **Node.js** (opcional): Versão 18.x ou superior, caso deseje executar ou modificar as aplicações localmente fora do Docker.
- **Git**: Para clonar o repositório do projeto.

### Passo a Passo Detalhado
1. **Clonar o Repositório**
   Abra um terminal e execute os seguintes comandos para baixar o código-fonte do projeto:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd benchmark-frameworks
   ```
   Substitua `<URL_DO_REPOSITORIO>` pelo endereço real do repositório (ex.: `https://github.com/seu-usuario/seu-repositorio.git`).

2. **Construir as Aplicações**
   Execute o comando abaixo para construir os artefatos de produção de cada aplicação (React, Vue e Angular):
   ```bash
   docker-compose -f docker-compose-build.yml up
   ```
   Este comando cria contêineres temporários que instalam as dependências (`npm install`) e geram os arquivos otimizados (`npm run build`) em cada diretório `dist`. Após a conclusão, os contêineres são encerrados automaticamente.

3. **Rodar o Ambiente de Produção/Teste**
   Para iniciar os serviços de teste e executar os benchmarks, use:
   ```bash
   docker-compose -f docker-compose.yml up
   ```
   - **O que acontece**: Os contêineres Nginx são iniciados para servir as aplicações nas portas `8080` (React), `8081` (Vue) e `8082` (Angular). O contêiner Lighthouse aguarda a disponibilidade dos serviços (via healthcheck) e executa os benchmarks, salvando os relatórios na pasta `results`.
   - **Acesse as aplicações**: Abra um navegador e visite:
     - React: `http://localhost:8080`
     - Vue: `http://localhost:8081`
     - Angular: `http://localhost:8082`
   - **Verifique os resultados**: Após a execução, os relatórios do Lighthouse estarão disponíveis em `results` (ex.: `react-report.json`, `vue-report.json`).

4. **Rodar o Ambiente de Desenvolvimento (Opcional)**
   Se desejar trabalhar no código com recarga automática, execute:
   ```bash
   docker-compose -f docker-compose-dev.yml up
   ```
   - **O que acontece**: Os contêineres Node.js iniciam as aplicações em modo de desenvolvimento nas portas `3000` (React), `3001` (Vue) e `3002` (Angular), com hot-reload ativado para refletir mudanças no código em tempo real.
   - **Acesse as aplicações**: No navegador:
     - React: `http://localhost:3000`
     - Vue: `http://localhost:3001`
     - Angular: `http://localhost:3002`

5. **Parar os Contêineres**
   Para encerrar os serviços e liberar os recursos, pressione `Ctrl+C` no terminal e, em seguida, execute:
   ```bash
   docker-compose -f <NOME_DO_ARQUIVO> down
   ```
   Substitua `<NOME_DO_ARQUIVO>` pelo arquivo correspondente (`docker-compose.yml` ou `docker-compose-dev.yml`). Isso remove os contêineres, mas preserva os volumes e imagens para reutilização futura.

---

## Requisitos de Sistema

O projeto foi desenvolvido e testado em um sistema com as seguintes especificações detalhadas. Recomenda-se um hardware equivalente ou superior para garantir uma execução fluida:

- **Sistema Operacional**: Compatível com Windows (10 ou 11), macOS (qualquer versão recente) ou distribuições Linux (ex.: Ubuntu 20.04 ou superior).
- **CPU**: Intel® Core™ i5-8400 @ 2.80GHz.
  - **Detalhes**: 6 núcleos, 6 threads, arquitetura Coffee Lake (14 nm), frequência base de 2.80 GHz e máxima de 3.80 GHz com Turbo Boost. Suporta extensões como MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, EM64T, AES, AVX, AVX2 e FMA3. Cache: L1D 32 KB, L2 256 KB, L3 9216 KB.
  - **TDP**: 65 Watts, com tensão (Vcore) de 1.044 Volts.
  - **Temperatura**: Média de 53 °C sob carga leve durante os testes.
- **Memória RAM**: 16 GB (16384 MB) DDR4-SDRAM.
  - **Detalhes**: Dual Channel (128 bits), frequência de 1200.4 MHz (DDR4-2400), timings 15-15-15-35-2 (tCAS-tRCD-tRP-tRAS-tCR). Dois módulos Kingston de 8 GB cada (P/N: KHX2400C15/8G, XMP 2.0).
- **Armazenamento**: 2 SSDs SATA de 240 GB cada.
  - **Modelo 1**: SanDisk SSD PLUS 240 GB (Firmware: UF3600RL), capacidade de 223.6 GiB.
  - **Modelo 2**: KINGSTON SA400S37240G (Firmware: SBFKB1D1), capacidade de 223.6 GiB.
- **GPU**: NVIDIA GeForce GTX 1660 + Intel UHD Graphics 630 (integrada).
  - **NVIDIA GTX 1660**: TU116-300, 12 nm, 6.6 bilhões de transistores, 284 mm², TDP 120W. 1408 Shader Units, 88 TMUs, 48 ROPs, 6 GB GDDR5 (4001 MHz, 192-bit). Suporta DirectX 12.1, OpenGL 4.6, OpenCL 1.2, Vulkan 1.1.
  - **Intel UHD Graphics 630**: GPU integrada ao Coffee Lake, usada como fallback.
- **Placa-mãe**: Gigabyte H310M S2P 2.0.
  - **Detalhes**: Socket 1151 LGA, North Bridge Intel Coffee Lake (rev 07), South Bridge Intel H310 (rev 00), BIOS AMI F11 (03/08/2019).
- **Docker**: Versão 20.10 ou superior, necessário para criar e gerenciar os contêineres.
- **Docker Compose**: Versão 1.29 ou superior, para orquestração dos serviços.
- **Espaço em Disco**: Mínimo de 5 GB livres para imagens Docker, dependências e artefatos de build.
- **Conexão de Rede**: Não é estritamente necessária para execução local, mas útil para baixar imagens Docker na primeira vez.

Essas especificações foram suficientes para rodar todos os contêineres simultaneamente (desenvolvimento, build e teste) sem gargalos significativos. Para sistemas com menos recursos (ex.: 4 GB de RAM ou CPU dual-core), recomenda-se executar apenas um serviço por vez (ex.: apenas o React) para evitar sobrecarga.

---

## Metodologia

O desenvolvimento deste trabalho seguiu uma metodologia estruturada, dividida em etapas claras para garantir a consistência e a validade dos resultados:

1. **Definição do Escopo**: 
   - Escolhi uma aplicação "to-do list" como caso de teste devido à sua simplicidade e universalidade. A aplicação inclui funcionalidades básicas: adicionar uma tarefa, remover uma tarefa e listar todas as tarefas. Isso permitiu focar nas características dos frameworks sem introduzir complexidades desnecessárias.
2. **Seleção de Tecnologias**: 
   - Os frameworks ReactJS, Angular e Vue.js foram selecionados por sua relevância no mercado e diferenças arquiteturais. O **Redux Toolkit** foi adotado como solução de gerenciamento de estado para padronizar a lógica entre os projetos. **TypeScript** foi usado para robustez, e **Tailwind CSS** para estilização rápida e consistente.
3. **Implementação**: 
   - Desenvolvi a mesma aplicação "to-do list" em cada framework, mantendo as funcionalidades idênticas. O código foi estruturado em componentes reutilizáveis (React e Vue) ou módulos (Angular), com o estado gerenciado via Redux Toolkit (ex.: um slice para tarefas com ações `addTask` e `removeTask`).
4. **Configuração da Infraestrutura**: 
   - Utilizei Docker para criar ambientes isolados para cada aplicação, com Nginx como proxy reverso para servir os artefatos de build. O Vite foi usado como ferramenta de build para React e Vue, enquanto o Angular CLI foi mantido para o Angular devido à sua integração nativa. Três arquivos Docker Compose foram criados para separar as fases de build, desenvolvimento e teste.
5. **Benchmarks**: 
   - Configurei o Lighthouse em um contêiner Docker para executar benchmarks automatizados em cada aplicação. Os testes foram realizados em um ambiente controlado (laboratório), com o Nginx servindo as páginas e o Lighthouse coletando métricas como FCP, LCP e TBT. Os relatórios foram salvos em formato JSON na pasta `results`.
6. **Análise dos Resultados**: 
   - Analisei os relatórios do Lighthouse para comparar os frameworks em termos quantitativos (métricas de desempenho) e qualitativos (facilidade de implementação, clareza do código). Também considerei fatores como o tamanho do bundle gerado e o tempo de build.

Essa metodologia garantiu que os resultados fossem comparáveis, replicáveis e alinhados aos objetivos do TCC.

---

## Exemplo de Uso Prático

Para ilustrar como utilizar o projeto na prática, aqui está um guia passo a passo com um exemplo concreto:

1. **Construa as Aplicações**:
   Execute o comando para gerar os artefatos de produção:
   ```bash
   docker-compose -f docker-compose-build.yml up
   ```
   Isso instala as dependências e compila cada aplicação, gerando os arquivos em `dist`.

2. **Inicie o Ambiente de Teste**:
   Inicie os serviços de produção/teste:
   ```bash
   docker-compose -f docker-compose.yml up
   ```
   Os contêineres Nginx iniciam e o Lighthouse executa os benchmarks automaticamente.

3. **Acesse as Aplicações**:
   Abra um navegador e visite os seguintes endereços para verificar as aplicações em funcionamento:
   - React: `http://localhost:8080`
   - Vue: `http://localhost:8081`
   - Angular: `http://localhost:8082`
   Você verá a interface da "to-do list" com campos para adicionar tarefas e uma lista atualizada em tempo real.

4. **Verifique os Resultados**:
   Após a execução, vá até a pasta `results` e abra um relatório, como `react-report.json`. Um exemplo de conteúdo seria:
   ```json
   {
     "first-contentful-paint": 1.2,
     "largest-contentful-paint": 2.5,
     "total-blocking-time": 0.1,
     "cumulative-layout-shift": 0.02,
     "interaction-to-next-paint": 0.05,
     "time-to-first-byte": 0.3,
     "performance-score": 92
   }
   ```
   - **Interpretação**: 
     - `first-contentful-paint` (1.2s): Tempo até o primeiro conteúdo visível.
     - `largest-contentful-paint` (2.5s): Tempo até o maior elemento ser renderizado.
     - `total-blocking-time` (0.1s): Tempo de bloqueio da thread principal.
     - `cumulative-layout-shift` (0.02): Estabilidade do layout (quanto menor, melhor).
     - `interaction-to-next-paint` (0.05s): Latência das interações.
     - `time-to-first-byte` (0.3s): Tempo de resposta do servidor.
     - `performance-score` (92): Pontuação geral de desempenho (0-100).
   Repita a análise para os relatórios de Vue e Angular e compare os valores para determinar qual framework oferece o melhor desempenho no seu caso de uso.

Este exemplo demonstra como o projeto pode ser usado para avaliar frameworks em um cenário realista.

---

## Métricas Analisadas

As seguintes métricas foram coletadas pelo Lighthouse para avaliar o desempenho das aplicações, com definições detalhadas:

1. **First Contentful Paint (FCP)**: 
   - **Definição**: Mede o tempo entre o início do carregamento da página e o momento em que qualquer parte do conteúdo (texto, imagem) é renderizada na tela.
   - **Relevância**: Indica a percepção inicial de velocidade pelo usuário.
   - **Contexto**: Testado em laboratório e campo simulado.
2. **Largest Contentful Paint (LCP)**: 
   - **Definição**: Mede o tempo até que o maior bloco de texto ou elemento de imagem seja renderizado.
   - **Relevância**: Reflete o carregamento do conteúdo principal.
   - **Contexto**: Testado em laboratório e campo simulado.
3. **Interaction to Next Paint (INP)**: 
   - **Definição**: Mede a latência de interações (cliques, toques, teclas) e seleciona a pior latência como valor representativo.
   - **Relevância**: Avalia a capacidade de resposta da página.
   - **Contexto**: Testado em laboratório e campo simulado.
4. **Total Blocking Time (TBT)**: 
   - **Definição**: Soma o tempo entre FCP e o Time to Interactive (TTI) em que a thread principal fica bloqueada, impedindo interações.
   - **Relevância**: Indica a interatividade da página.
   - **Contexto**: Testado em laboratório.
5. **Cumulative Layout Shift (CLS)**: 
   - **Definição**: Calcula a pontuação cumulativa de mudanças inesperadas no layout durante o carregamento.
   - **Relevância**: Mede a estabilidade visual.
   - **Contexto**: Testado em laboratório e campo simulado.
6. **Time to First Byte (TTFB)**: 
   - **Definição**: Tempo que a rede leva para responder com o primeiro byte de um recurso.
   - **Relevância**: Reflete a latência do servidor.
   - **Contexto**: Testado em laboratório e campo simulado.

Essas métricas foram analisadas em um ambiente controlado (laboratório) e em condições simuladas de campo (ex.: latência de rede artificial), oferecendo uma visão abrangente do desempenho dos frameworks.

---

## Perguntas Respondidas pelo Trabalho

O TCC aborda três questões principais, com respostas detalhadas baseadas nos resultados obtidos:

1. **QP1: É possível implementar benchmarks para frontend utilizando infraestrutura com código?**
   - **Resposta**: Sim, é plenamente possível implementar benchmarks para frontend utilizando infraestrutura como código (IaC). Neste projeto, utilizei contêineres Docker para encapsular as aplicações (React, Vue, Angular) e a ferramenta Lighthouse, garantindo um ambiente consistente e isolado. Os arquivos Docker Compose definem a infraestrutura de forma declarativa, permitindo a execução automatizada dos benchmarks. Uma alternativa viável seria o uso do Podman, uma ferramenta sem daemon que também suporta contêineres via runtime `containerd`, oferecendo compatibilidade com a mesma padronização OCI (Open Container Initiative).
2. **QP2: Que métricas podem ser extraídas durante e após a execução do ambiente?**
   - **Resposta**: Após a execução bem-sucedida do Lighthouse no ambiente proposto, os relatórios gerados em formato JSON contêm uma ampla gama de métricas de desempenho. As principais incluem: **First Contentful Paint (FCP)**, que mede o tempo até o primeiro conteúdo visível; **Largest Contentful Paint (LCP)**, que avalia o carregamento do conteúdo principal; **Interaction to Next Paint (INP)**, que analisa a latência das interações; **Total Blocking Time (TBT)**, que quantifica o bloqueio da thread principal; **Cumulative Layout Shift (CLS)**, que verifica a estabilidade do layout; e **Time to First Byte (TTFB)**, que reflete a resposta do servidor. Além disso, o Lighthouse fornece pontuações gerais de desempenho, acessibilidade, boas práticas e SEO, enriquecendo a análise.
3. **QP3: Que frameworks frontend é possível testar dentro deste arcabouço criado?**
   - **Resposta**: O arcabouço foi projetado e testado com os frameworks **React**, **Angular** e **Vue**, que foram implementados com sucesso na aplicação "to-do list". No entanto, a infraestrutura é flexível e expansível, permitindo a inclusão de outros frameworks frontend ou full-stack, como Svelte, SolidJS, Next.js ou Nuxt.js, com ajustes mínimos nos arquivos Docker Compose e nas configurações de build. A padronização com Redux Toolkit e TypeScript facilita a adaptação de novos frameworks ao projeto.

Essas respostas validam a viabilidade técnica e a utilidade prática da solução proposta.

---

## Resultados Esperados

Os benchmarks geram relatórios detalhados que permitem uma comparação abrangente entre os frameworks em três dimensões principais:
- **Desempenho**: Identificar qual framework oferece os menores tempos de carregamento (FCP, LCP, TTFB), menor latência nas interações (INP) e maior interatividade (TBT baixo). Por exemplo, um framework com LCP abaixo de 2.5 segundos é considerado ideal para uma boa experiência do usuário.
- **Facilidade de Uso**: Avaliar qual framework é mais intuitivo e produtivo para implementar a "to-do list", considerando a clareza da documentação, a simplicidade da API e o tempo necessário para configurar o projeto com Redux Toolkit e Tailwind CSS.
- **Eficiência**: Determinar qual framework consome menos recursos (ex.: tamanho do bundle gerado após o build) e oferece melhor escalabilidade em cenários de uso intensivo, como múltiplas requisições simultâneas ao Nginx.

Os resultados estão disponíveis na pasta `results` após a execução do Lighthouse, em arquivos como `react-report.json`, `vue-report.json` e `angular-report.json`. Esses dados podem ser usados para tomar decisões informadas sobre a escolha de um framework para projetos específicos.

---

## Limitações do Trabalho

Embora o projeto tenha alcançado seus objetivos, algumas limitações foram identificadas durante o desenvolvimento e análise:
- **Escopo da Aplicação**: A "to-do list" é uma aplicação simples, com funcionalidades básicas (adicionar, remover, listar tarefas). Isso pode não refletir o desempenho dos frameworks em projetos mais complexos, como aplicações com animações avançadas, integração com APIs externas ou grandes volumes de dados.
- **Cenários de Teste**: Os benchmarks foram realizados em um ambiente controlado (laboratório), sem simulação de condições reais como redes instáveis, latência variável ou tráfego de usuários simultâneos. Isso limita a generalização dos resultados para cenários de produção.
- **Frameworks Testados**: Apenas React, Angular e Vue foram avaliados, excluindo outros frameworks populares como Svelte, SolidJS ou soluções full-stack como Next.js e Nuxt.js, que poderiam oferecer perspectivas diferentes.
- **Recursos de Hardware**: Os testes foram executados em uma máquina específica (Intel i5-8400, 16 GB RAM), e os resultados podem variar em sistemas com especificações diferentes, como CPUs mais lentas ou menos memória disponível.

Essas limitações não comprometem a validade do trabalho, mas indicam áreas que podem ser exploradas em estudos futuros para ampliar o escopo e a aplicabilidade dos resultados.

---

## Comparação com Outras Abordagens

A abordagem deste TCC difere de métodos tradicionais de benchmarking de frameworks frontend, oferecendo vantagens específicas:
- **Testes Manuais com DevTools**: Ferramentas como o Chrome DevTools permitem medir métricas como FCP e TBT manualmente, mas são propensas a erros humanos, falta de automação e inconsistências entre execuções. Este projeto automatiza os testes com Lighthouse e Docker, garantindo precisão e repetibilidade.
- **Plataformas Online (ex.: WebPageTest)**: Serviços como WebPageTest oferecem benchmarks detalhados, mas dependem de conexão com a internet e não permitem controle total sobre o ambiente (ex.: versões de software, configurações de servidor). Aqui, o uso de Docker e Nginx proporciona um ambiente local e personalizável.
- **Scripts Personalizados**: Alguns desenvolvedores criam scripts para medir desempenho, mas esses exigem esforço significativo para configuração, manutenção e portabilidade. A infraestrutura como código (IaC) deste TCC, baseada em Docker Compose, simplifica a execução e adaptação do projeto.

A combinação de Docker, Nginx e Lighthouse resulta em uma solução que equilibra automação, consistência e replicabilidade, tornando-a mais prática e escalável para uso acadêmico e profissional.

---

## Contribuições e Melhorias Futuras

O projeto abre caminho para várias possibilidades de expansão e aprimoramento:
- **Adição de Novos Frameworks**: Incluir frameworks como Svelte (focado em desempenho), SolidJS (leve e reativo) ou soluções full-stack como Next.js e Nuxt.js para uma análise mais abrangente.
- **Testes de Carga**: Integrar ferramentas como Artillery ou Locust para simular tráfego intenso e avaliar a escalabilidade dos frameworks sob condições de uso realistas.
- **Expansão da Aplicação**: Adicionar funcionalidades mais complexas à "to-do list", como filtros, categorias, persistência em banco de dados ou animações, para testar os frameworks em cenários mais desafiadores.
- **Simulação de Rede**: Configurar o Docker para simular latências de rede ou condições instáveis, aproximando os testes de cenários de produção.
- **Otimização do Nginx**: Explorar configurações avançadas de cache e balanceamento de carga para melhorar o desempenho em cenários de alta demanda.

Essas melhorias podem tornar o arcabouço ainda mais robusto e útil para a comunidade de desenvolvimento.

---

## Instruções para Contribuidores

Se você deseja contribuir com este projeto, siga estas etapas detalhadas:
1. **Faça um Fork**: Acesse o repositório no GitHub, clique em "Fork" e crie uma cópia no seu perfil.
2. **Clone o Repositório**: No terminal, execute:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd benchmark-frameworks
   ```
3. **Crie uma Branch**: Crie uma nova branch para sua contribuição:
   ```bash
   git checkout -b minha-feature
   ```
4. **Realize as Alterações**: Edite o código ou a documentação conforme necessário (ex.: adicione um novo framework, ajuste o Dockerfile).
5. **Commit**: Salve suas mudanças com uma mensagem descritiva:
   ```bash
   git add .
   git commit -m "Adiciona suporte ao framework Svelte"
   ```
6. **Push**: Envie a branch para o seu fork:
   ```bash
   git push origin minha-feature
   ```
7. **Envie um Pull Request**: No GitHub, abra um pull request para o repositório original, descrevendo detalhadamente o que foi feito e por quê.

**Sugestões de Contribuições**:
- Adicionar suporte a novos frameworks ou bibliotecas.
- Melhorar a configuração do Nginx com cache ou compressão.
- Integrar ferramentas adicionais de análise (ex.: Web Vitals).
- Criar scripts para automatizar a comparação dos relatórios do Lighthouse.

---

## Capturas de Tela ou Diagramas

### Interface da Aplicação "To-Do List"
- **React**: ![To-Do List no React](screenshots/react-todo.png) *(A ser adicionado)*  
  Uma interface simples com um campo de entrada para novas tarefas e uma lista renderizada dinamicamente.
- **Vue**: ![To-Do List no Vue](screenshots/vue-todo.png) *(A ser adicionado)*  
  Similar ao React, mas com a sintaxe e estilo característicos do Vue.
- **Angular**: ![To-Do List no Angular](screenshots/angular-todo.png) *(A ser adicionado)*  
  Implementação com diretivas Angular e estilização Tailwind.

### Arquitetura da Infraestrutura
- **Diagrama**: ![Diagrama da Infraestrutura](diagrams/infrastructure.png) *(A ser adicionado)*  
  Representação visual dos contêineres Docker (React, Vue, Angular, Nginx, Lighthouse), com setas indicando o fluxo de requisições via proxy reverso e a geração de relatórios.

*Nota*: As imagens ainda não estão incluídas. Criarei pastas `screenshots` e `diagrams` no repositório, adicione os arquivos correspondentes e atualizarei os caminhos acima.

---

## Autor

- **Nome**: Lucas Martins Mororó
- **Curso**: Ciência da Computação
- **Instituição**: UVA - Universidade Estadual do Vale do Acaraú
- **Contato**: lucasmmororo@gmail.com
<!-- - **Orientador**: [Nome do Orientador] -->

---

## Agradecimentos

Gostaria de expressar minha gratidão às seguintes pessoas e entidades que tornaram este trabalho possível:
- **Orientador**: [Nome do Orientador], por sua orientação valiosa, feedback construtivo e apoio durante todo o processo de desenvolvimento do TCC.
- **Família e Amigos**: Pelo suporte emocional e incentivo ao longo do curso.
- **Comunidade Open-Source**: Pelas ferramentas incríveis como Docker, Nginx, Lighthouse, React, Angular, Vue e Redux Toolkit, que formam a base técnica deste projeto.
- **Colegas de Curso**: Por discussões e trocas de ideias que enriqueceram minha perspectiva sobre desenvolvimento web.

---

## Referências

Abaixo estão as principais fontes e documentações consultadas durante o desenvolvimento do projeto:
- **React**: [https://react.dev/](https://react.dev/) - Documentação oficial do React.
- **Angular**: [https://angular.dev/](https://angular.dev/) - Documentação oficial do Angular.
- **Vue.js**: [https://vuejs.org/](https://vuejs.org/) - Documentação oficial do Vue.js.
- **Redux Toolkit**: [https://redux-toolkit.js.org/](https://redux-toolkit.js.org/) - Guia oficial do Redux Toolkit.
- **Tailwind CSS**: [https://tailwindcss.com/](https://tailwindcss.com/) - Documentação do Tailwind CSS.
- **Vite**: [https://vitejs.dev/](https://vitejs.dev/) - Documentação oficial do Vite.
- **Docker**: [https://docs.docker.com/](https://docs.docker.com/) - Documentação oficial do Docker.
- **Nginx**: [https://nginx.org/](https://nginx.org/) - Site oficial do Nginx.
- **Lighthouse**: [https://developers.google.com/web/tools/lighthouse](https://developers.google.com/web/tools/lighthouse) - Documentação do Lighthouse pelo Google.

---

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE), permitindo uso, modificação e distribuição livre, desde que os créditos sejam mantidos. Consulte o arquivo `LICENSE` para mais detalhes.
