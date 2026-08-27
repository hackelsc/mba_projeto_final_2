from dagster import asset

from scripts.camada_duckdb import gerar_duckdb

NOME_ARQUIVO = "preco_primeiro_semestre_2026.parquet"


@asset(description="Copia da Gold dentro de um banco DuckDB, para consulta via SQL no dashboard.")
def duckdb_combustiveis(gold_combustiveis: str) -> str:
    caminho = gerar_duckdb(NOME_ARQUIVO)
    return str(caminho)
