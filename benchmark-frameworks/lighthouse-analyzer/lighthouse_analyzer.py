import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple

# Configura o estilo dos gráficos para visualização de qualidade de publicação
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")


class LighthouseAnalyzer:
    """
    Classe responsável por carregar, processar e visualizar os dados de performance
    obtidos por meio de relatórios JSON do Lighthouse para diferentes frameworks web.
    """

    def __init__(self, results_dir: str = './results'):
        """
        Inicializa a classe com o diretório onde estão os relatórios JSON divididos
        em subdiretórios por framework.

        Args:
            results_dir (str): Caminho para a pasta com os relatórios.
        """
        self.results_dir = Path(results_dir)
        self.frameworks = ['react', 'vue', 'angular']  # Frameworks analisados
        self.metrics = {  # Métricas que serão extraídas dos relatórios
            'first-contentful-paint': {'name': 'First Contentful Paint (FCP)', 'unit': 'ms'},
            'largest-contentful-paint': {'name': 'Largest Contentful Paint (LCP)', 'unit': 'ms'},
            'interaction-to-next-paint': {'name': 'Interaction to Next Paint (INP)', 'unit': 'ms'},
            'total-blocking-time': {'name': 'Total Blocking Time (TBT)', 'unit': 'ms'},
            'cumulative-layout-shift': {'name': 'Cumulative Layout Shift (CLS)', 'unit': 'score'},
            'server-response-time': {'name': 'Time to First Byte (TTFB)', 'unit': 'ms'}
        }
        self.data = {}  # Dicionário para armazenar os dados carregados

    def load_json_reports(self) -> Dict:
        """
        Carrega os arquivos JSON de cada framework e os organiza em um dicionário.

        Returns:
            Dict: Dados organizados por framework.
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
        Extrai as métricas dos relatórios carregados e os organiza em um DataFrame.

        Returns:
            pd.DataFrame: Métricas por framework e execução.
        """
        print("[INFO] Extraindo métricas de performance...")
        metrics_data = []

        for framework, reports in self.data.items():
            for run_idx, report in enumerate(reports, 1):
                row = {'framework': framework, 'run': run_idx}

                for metric_key, metric_info in self.metrics.items():
                    try:
                        audit_data = report['audits'].get(metric_key, {})
                        value = audit_data.get('numericValue')
                        row[metric_key] = value if value is not None else None
                    except KeyError:
                        row[metric_key] = None

                metrics_data.append(row)

        df = pd.DataFrame(metrics_data)
        print(f"[OK] Métricas extraídas de {len(df)} execuções")
        return df

    def calculate_averages(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Calcula a média e desvio padrão de cada métrica por framework.

        Args:
            df (pd.DataFrame): Dados brutos de métricas.

        Returns:
            pd.DataFrame: Estatísticas por framework.
        """
        print("[INFO] Calculando médias e desvios padrão...")
        metric_columns = list(self.metrics.keys())
        averages = df.groupby('framework')[metric_columns].agg(['mean', 'std']).round(2)
        averages.columns = [f"{col[0]}_{col[1]}" for col in averages.columns]
        averages = averages.reset_index()
        print("[OK] Cálculos finalizados")
        return averages

    def create_comparison_chart(self, df: pd.DataFrame, output_dir: str = './charts') -> None:
        """
        Cria um gráfico comparativo para todas as métricas analisadas.

        Args:
            df (pd.DataFrame): Dados brutos de métricas
            output_dir (str): Pasta onde salvar os gráficos
        """
        print("[INFO] Criando gráfico comparativo de desempenho...")
        Path(output_dir).mkdir(exist_ok=True)
        averages = df.groupby('framework')[list(self.metrics.keys())].mean()

        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Comparativo de Performance entre Frameworks - Core Web Vitals', fontsize=16, fontweight='bold')
        axes = axes.flatten()

        for idx, (metric_key, metric_info) in enumerate(self.metrics.items()):
            ax = axes[idx]
            frameworks = averages.index
            values = averages[metric_key]
            bars = ax.bar(frameworks, values, alpha=0.8, edgecolor='black', linewidth=0.5)
            colors = ['#e74c3c', '#3498db', '#2ecc71']

            for bar, color in zip(bars, colors):
                bar.set_color(color)

            for bar, value in zip(bars, values):
                if not pd.isna(value):
                    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + bar.get_height()*0.01,
                            f'{value:.1f}', ha='center', va='bottom', fontweight='bold')

            ax.set_title(metric_info['name'], fontweight='bold', fontsize=12)
            ax.set_ylabel(f"Tempo ({metric_info['unit']})" if metric_info['unit'] == 'ms' else metric_info['unit'])
            ax.grid(True, alpha=0.3, axis='y')
            ax.set_xticklabels([f.capitalize() for f in frameworks])

        plt.tight_layout()
        plt.savefig(f"{output_dir}/performance_comparison.png", dpi=300, bbox_inches='tight')
        plt.savefig(f"{output_dir}/performance_comparison.pdf", bbox_inches='tight')
        print(f"[OK] Gráfico salvo em {output_dir}/performance_comparison.png")

    # DICA: adicione os outros métodos com o mesmo padrão, se desejar

    def run_complete_analysis(self) -> None:
        """
        Executa todo o pipeline: carregamento dos dados, cálculo das métricas,
        geração de gráficos e criação do relatório final.
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
        self.create_comparison_chart(df, output_dir)
        # Se quiser, adicione também:
        # self.create_core_web_vitals_chart(...)
        # self.create_detailed_table(...)
        # self.generate_summary_report(...)
        print(f"\n[FINALIZADO] Análise concluída! Resultados disponíveis em '{output_dir}'")


def main():
    """
    Função principal que inicia o processo completo de análise.
    """
    # Caminho absoluto para sua pasta de resultados
    analyzer = LighthouseAnalyzer('C:/Users/Lucas/Desktop/TCC/benchmark-frameworks/results')
    analyzer.run_complete_analysis()


if __name__ == "__main__":
    main()
