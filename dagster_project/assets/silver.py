# TODO (Pessoa 2): implementar o asset de Silver aqui, seguindo o mesmo padrao
# de assets/bronze.py -- a logica de verdade deve morar em scripts/silver.py,
# e este arquivo so embrulha ela como asset do Dagster.
#
# from dagster import asset
# from scripts.silver import gerar_silver
#
# @asset(description="Dados limpos e tipados.")
# def silver_combustiveis(bronze_combustiveis: str) -> str:
#     caminho = gerar_silver()
#     return str(caminho)
