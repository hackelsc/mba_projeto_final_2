from dagster import asset

from scripts.bronze import gerar_bronze

NOME_ARQUIVO = "preco_primeiro_semestre_2026.csv"


@asset(description="Dados tecnicos em Parquet: colunas renomeadas, ainda sem limpeza de valores.")
def bronze_combustiveis() -> str:
    caminho = gerar_bronze(NOME_ARQUIVO)
    return str(caminho)
