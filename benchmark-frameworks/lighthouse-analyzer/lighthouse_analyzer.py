# -*- coding: utf-8 -*-

import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple

# Define o estilo dos gráficos para uma visualização agradável e profissional
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")


class LighthouseAnalyzer:
    """
    Classe que carrega, processa e visualiza dados de performance dos relatórios
    do Lighthouse (formato JSON), geralmente usados para medir desempenho de páginas web.
    """

    def __init__(self, results_dir: str = './results'):
        """
        Inicializa a classe com o diretório de resultados contendo relatórios por framework.

        Args:
            results_dir (str): Caminho para a pasta com os relatórios JSON organizados por framework.
        """
        self.results_dir = Path(results_dir)
        self.frameworks = ['react', 'vue', 'angular']  # Frameworks analisados

        # Métricas selecionadas e seus nomes legíveis e unidades
        self.metrics = {
            # Quanto tempo leva para o primeiro conteúdo visual aparecer na tela (texto, imagem, etc.)
            'first-contentful-paint': {'name': 'First Contentful Paint (FCP)', 'unit': 'ms'},

            # Quanto tempo leva para o maior elemento visível da tela ser carregado (como imagem ou título grande)
            'largest-contentful-paint': {'name': 'Largest Contentful Paint (LCP)', 'unit': 'ms'},

            # Soma de todos os atrasos causados por JavaScript que bloqueia a interação com a página
            'total-blocking-time': {'name': 'Total Blocking Time (TBT)', 'unit': 'ms'},

            # Tempo entre o início da navegação e o recebimento do primeiro byte do servidor
            'server-response-time': {'name': 'Time to First Byte (TTFB)', 'unit': 'ms'},

            # Velocidade geral do carregamento da página, combinando várias fases (quanto menor, melhor)
            'speed-index': {'name': 'Speed Index (SI)', 'unit': 'ms'},

            # Quando o conteúdo principal da página está visivelmente carregado (nem sempre confiável, mas útil)
            'first-meaningful-paint': {'name': 'First Meaningful Paint (FMP)', 'unit': 'ms'},

            # Quando o HTML foi completamente carregado e analisado, e o DOM foi construído (sem esperar por CSS/imagens)
            'dom-content-loaded': {'name': 'DOM Content Loaded (DCL)', 'unit': 'ms'},  # vem de metrics → observedDomContentLoaded

            # Quando a página está completamente pronta para o usuário interagir (clicar, digitar, etc.)
            'interactive': {'name': 'Time to Interactive (TTI)', 'unit': 'ms'},

            # Maior tempo potencial que o navegador pode levar para responder à primeira interação do usuário
            'max-potential-fid': {'name': 'Max Potential FID', 'unit': 'ms'},

            # Tempo total que o navegador levou para analisar e executar JavaScript durante o carregamento
            'bootup-time': {'name': 'JS Boot-up Time', 'unit': 'ms'}
        }

        self.data = {}  # Armazena os dados carregados por framework

    def load_json_reports(self) -> Dict:
        """
        Carrega todos os relatórios JSON dos frameworks encontrados no diretório.
        
        Returns:
            Dict: Dicionário com os dados por framework.
        """
        print("[INFO] Carregando relatórios JSON do Lighthouse...")

        for framework in self.frameworks:
            framework_dir = self.results_dir / framework

            if not framework_dir.exists():
                print(f"[WARN] Diretório {framework_dir} não encontrado")
                continue

            self.data[framework] = []
            json_files = list(framework_dir.glob(f"{framework}-run-*.json"))

            if not json_files:
                print(f"[WARN] Nenhum arquivo JSON encontrado para {framework}")
                continue

            for json_file in sorted(json_files):
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        report_data = json.load(f)
                        self.data[framework].append(report_data)
                except Exception as e:
                    print(f"[ERRO] Falha ao carregar {json_file}: {e}")

            print(f"[OK] {len(self.data[framework])} relatórios carregados para {framework}")

        return self.data

    def extract_metrics(self) -> pd.DataFrame:
        """
        Extrai as métricas configuradas de todos os relatórios carregados.

        Returns:
            pd.DataFrame: DataFrame com métricas por framework e execução.
        """
        print("[INFO] Extraindo métricas de performance...")
        metrics_data = []  # Lista onde cada item será uma linha do DataFrame

        for framework, reports in self.data.items():
            for run_idx, report in enumerate(reports, 1):
                row = {'framework': framework, 'run': run_idx}  # Cria linha inicial com nome e execução

                for metric_key, metric_info in self.metrics.items():
                    # DOM Content Loaded é uma métrica especial que vem dentro de 'metrics'
                    if metric_key == 'dom-content-loaded':
                        try:
                            row[metric_key] = report['audits']['metrics']['details']['items'][0]['observedDomContentLoaded']
                        except KeyError:
                            print(f"[DEBUG] dom-content-loaded não encontrada para {framework} execução {run_idx}")
                            row[metric_key] = None
                    else:
                        # Métricas padrão vêm de audits direto
                        audit_data = report.get('audits', {}).get(metric_key)
                        if audit_data and 'numericValue' in audit_data:
                            row[metric_key] = audit_data['numericValue']
                        else:
                            print(f"[DEBUG] Métrica '{metric_key}' ausente para {framework} execução {run_idx}")
                            row[metric_key] = None

                metrics_data.append(row)  # Adiciona linha à lista

        df = pd.DataFrame(metrics_data)  # Converte a lista em DataFrame do pandas
        print(f"[OK] Métricas extraídas de {len(df)} execuções")
        return df

    def calculate_averages(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calcula médias e desvios padrão de cada métrica para cada framework.

        Args:
            df (pd.DataFrame): DataFrame com métricas por execução.

        Returns:
            pd.DataFrame: Estatísticas agregadas (média e std).
        """
        print("[INFO] Calculando médias e desvios padrão...")
        metric_columns = list(self.metrics.keys())  # Nome das colunas com métricas

        # Agrupa por framework e calcula média e desvio padrão para cada métrica
        averages = df.groupby('framework')[metric_columns].agg(['mean', 'std']).round(2)
        averages.columns = [f"{col[0]}_{col[1]}" for col in averages.columns]  # Renomeia colunas
        averages = averages.reset_index()  # Coloca 'framework' de volta como coluna
        print("[OK] Cálculos finalizados")
        return averages

    def create_individual_metric_charts(self, df: pd.DataFrame, output_dir: str = './charts') -> None:
        """
        Gera e salva um gráfico de barras para cada métrica separadamente, comparando os frameworks.

        Args:
            df (pd.DataFrame): Dados brutos das métricas
            output_dir (str): Pasta onde os gráficos serão salvos
        """
        print("[INFO] Criando gráficos individuais por métrica...")
        Path(output_dir).mkdir(exist_ok=True)

        averages = df.groupby('framework')[list(self.metrics.keys())].mean()

        for metric_key, metric_info in self.metrics.items():
            plt.figure(figsize=(8, 5))
            values = averages[metric_key]
            bars = plt.bar(values.index, values.values, color=['#e74c3c', '#3498db', '#2ecc71'], edgecolor='black')

            # Adiciona os valores acima das barras
            for bar, value in zip(bars, values):
                if not pd.isna(value):
                    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.01,
                             f'{value:.1f}', ha='center', va='bottom', fontweight='bold')

            plt.title(metric_info['name'], fontsize=14, fontweight='bold')
            plt.ylabel(f"Tempo ({metric_info['unit']})")
            plt.grid(True, axis='y', alpha=0.3)
            plt.xticks(ticks=range(len(values.index)), labels=[f.capitalize() for f in values.index])

            filename = f"{output_dir}/{metric_key.replace('-', '_')}.png"
            plt.tight_layout()
            plt.savefig(filename, dpi=300)
            plt.close()
            print(f"[OK] Gráfico salvo: {filename}")

    def create_all_metrics_chart(self, df: pd.DataFrame, output_dir: str = './charts') -> None:
        """
        Gera e salva um gráfico de barras agrupadas com todas as métricas para cada framework.

        Args:
            df (pd.DataFrame): Dados brutos das métricas
            output_dir (str): Pasta onde o gráfico será salvo
        """
        print("[INFO] Criando gráfico com todas as métricas...")
        Path(output_dir).mkdir(exist_ok=True)

        # Calcula as médias por framework
        averages = df.groupby('framework')[list(self.metrics.keys())].mean()

        # Configurações do gráfico
        plt.figure(figsize=(12, 6))
        bar_width = 0.25  # Largura das barras
        frameworks = averages.index
        n_frameworks = len(frameworks)
        n_metrics = len(self.metrics)
        index = np.arange(n_metrics)  # Posições no eixo X para as métricas

        # Normaliza as métricas para o gráfico (escala entre 0 e 1 para lidar com diferentes unidades)
        normalized_data = averages.copy()
        for metric in self.metrics.keys():
            max_value = averages[metric].max()
            if max_value > 0:
                normalized_data[metric] = averages[metric] / max_value

        # Cria barras para cada framework
        colors = ['#e74c3c', '#3498db', '#2ecc71']  # Cores para React, Vue, Angular
        for i, framework in enumerate(frameworks):
            plt.bar(index + i * bar_width, normalized_data.loc[framework], bar_width, label=framework.capitalize(), color=colors[i], edgecolor='black')

        # Configura o gráfico
        plt.title('Comparação de Todas as Métricas por Framework (Normalizado)', fontsize=14, fontweight='bold')
        plt.xlabel('Métricas', fontsize=12)
        plt.ylabel('Valor Normalizado (0-1)', fontsize=12)
        plt.xticks(index + bar_width * (n_frameworks - 1) / 2, [self.metrics[m]['name'] for m in self.metrics.keys()], rotation=45, ha='right')
        plt.legend(title='Frameworks')
        plt.grid(True, axis='y', alpha=0.3)
        plt.tight_layout()

        # Salva o gráfico
        filename = f"{output_dir}/all_metrics_comparison.png"
        plt.savefig(filename, dpi=300)
        plt.close()
        print(f"[OK] Gráfico com todas as métricas salvo: {filename}")

    def create_comparison_chart(self, df: pd.DataFrame, output_dir: str = './charts') -> None:
        """
        Cria um gráfico comparativo com subgráficos para todas as métricas, mantendo o estilo dos gráficos individuais.

        Args:
            df (pd.DataFrame): Dados brutos das métricas.
            output_dir (str): Pasta onde o gráfico será salvo.
        """
        print("[INFO] Criando gráfico comparativo com todas as métricas...")
        Path(output_dir).mkdir(exist_ok=True)
        
        # Calcula as médias por framework
        averages = df.groupby('framework')[list(self.metrics.keys())].mean()
        
        # Define o layout dinâmico para subgráficos (baseado no número de métricas)
        n_metrics = len(self.metrics)
        n_cols = 3  # Número de colunas fixo (ajustável)
        n_rows = (n_metrics + n_cols - 1) // n_cols  # Calcula número de linhas necessário
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols * 6, n_rows * 4))
        fig.suptitle('Comparativo de Performance entre Frameworks - Todas as Métricas', fontsize=16, fontweight='bold')
        
        # Achata o array de eixos para facilitar iteração
        axes = axes.flatten() if n_metrics > 1 else [axes]
        
        # Cores consistentes com os gráficos individuais
        colors = ['#e74c3c', '#3498db', '#2ecc71']  # React, Vue, Angular
        
        for idx, (metric_key, metric_info) in enumerate(self.metrics.items()):
            if idx >= len(axes):
                break  # Evita acessar eixos inexistentes (segurança)
            
            ax = axes[idx]
            frameworks = averages.index
            values = averages[metric_key]
            
            # Cria barras
            bars = ax.bar(frameworks, values, color=colors, edgecolor='black', alpha=0.8)
            
            # Adiciona valores acima das barras
            for bar, value in zip(bars, values):
                if not pd.isna(value):
                    ax.text(
                        bar.get_x() + bar.get_width() / 2, 
                        bar.get_height() * 1.01,
                        f'{value:.1f}', 
                        ha='center', 
                        va='bottom', 
                        fontweight='bold'
                    )
            
            # Configurações do subgráfico
            ax.set_title(metric_info['name'], fontsize=12, fontweight='bold')
            ax.set_ylabel(f"Tempo ({metric_info['unit']})")
            ax.grid(True, axis='y', alpha=0.3)
            ax.set_xticks(range(len(frameworks)))
            ax.set_xticklabels([f.capitalize() for f in frameworks])
        
        # Desativa eixos não utilizados (se houver)
        for idx in range(len(self.metrics), len(axes)):
            axes[idx].set_visible(False)
        
        # Ajusta o layout para evitar sobreposição
        plt.tight_layout(rect=[0, 0, 1, 0.95])  # Deixa espaço para o título
        filename = f"{output_dir}/all_metrics_comparison.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"[OK] Gráfico comparativo salvo: {filename}")

    def run_complete_analysis(self) -> None:
        """
        Executa o pipeline completo: leitura dos dados, extração, média e visualização.
        """
        print("[INFO] Iniciando análise completa do Lighthouse...\n")
        self.load_json_reports()

        if not self.data:
            print("[ERRO] Nenhum dado encontrado. Verifique o diretório de resultados.")
            return

        df = self.extract_metrics()

        if df.empty:
            print("[ERRO] Nenhuma métrica extraída. Verifique os arquivos JSON.")
            return

        averages_df = self.calculate_averages(df)

        output_dir = './charts'
        Path(output_dir).mkdir(exist_ok=True)

        self.create_individual_metric_charts(df, output_dir)
        # self.create_all_metrics_chart(df, output_dir)  # Nova chamada para o gráfico combinado
        self.create_comparison_chart(df, output_dir)  # Chama o gráfico combinado

        df.to_csv(f"{output_dir}/raw_metrics.csv", index=False)
        print(f"[OK] Métricas exportadas para {output_dir}/raw_metrics.csv")

        print(f"\n[FINALIZADO] Análise concluída! Resultados disponíveis em '{output_dir}'")

def main():
    """
    Função principal que inicia o processo completo de análise.
    Basta alterar o caminho da pasta de resultados conforme necessário.
    """
    analyzer = LighthouseAnalyzer('C:/Users/Lucas/Desktop/TCC/benchmark-frameworks/results')
    analyzer.run_complete_analysis()

if __name__ == "__main__":
    main()
