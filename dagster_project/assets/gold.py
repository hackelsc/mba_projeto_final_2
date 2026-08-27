from dagster import asset

from scripts.gold import gerar_gold

NOME_ARQUIVO = "preco_primeiro_semestre_2026.parquet"


@asset(description="Dado limpo e enxuto (colunas relevantes + ano_mes), sem agregacao.")
def gold_combustiveis(silver_combustiveis: str) -> str:
    caminho = gerar_gold(NOME_ARQUIVO)
    return str(caminho)
