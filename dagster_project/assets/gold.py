# TODO (Pessoa 3): implementar o asset de Gold aqui, seguindo o mesmo padrao
# de assets/bronze.py -- a logica de verdade deve morar em scripts/gold.py,
# e este arquivo so embrulha ela como asset do Dagster.
#
# from dagster import asset
# from scripts.gold import gerar_gold
#
# @asset(description="Dado limpo e enxuto (colunas relevantes + ano_mes), sem agregacao.")
# def gold_combustiveis(silver_combustiveis: str) -> str:
#     caminho = gerar_gold("preco_primeiro_semestre_2026.parquet")
#     return str(caminho)
