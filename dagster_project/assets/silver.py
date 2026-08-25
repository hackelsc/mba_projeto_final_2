from dagster import asset

from scripts.silver import gerar_silver

NOME_ARQUIVO = "preco_primeiro_semestre_2026.parquet"

@asset(description="Dados limpos e tipados.")
def silver_combustiveis(bronze_combustiveis: str) -> str:
    caminho = gerar_silver(NOME_ARQUIVO)
    return str(caminho)

