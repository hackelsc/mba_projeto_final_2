from dagster import asset

from scripts.raw import gerar_raw

NOME_ARQUIVO = "preco_primeiro_semestre_2026.csv"


@asset(description="Copia bruta do CSV original da ANP, sem nenhuma transformacao.")
def raw_combustiveis() -> str:
    caminho = gerar_raw(NOME_ARQUIVO)
    return str(caminho)
