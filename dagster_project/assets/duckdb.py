# TODO (Pessoa 3): implementar o asset de DuckDB aqui, seguindo o mesmo
# padrao de assets/bronze.py -- a logica de verdade deve morar em
# scripts/camada_duckdb.py, e este arquivo so embrulha ela como asset do
# Dagster.
#
# from dagster import asset
# from scripts.camada_duckdb import gerar_duckdb
#
# @asset(description="Copia da Gold dentro de um banco DuckDB, para consulta via SQL no dashboard.")
# def duckdb_combustiveis(gold_combustiveis: str) -> str:
#     caminho = gerar_duckdb("preco_primeiro_semestre_2026.parquet")
#     return str(caminho)
