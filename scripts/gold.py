"""
Camada Gold: le o Parquet da Silver e seleciona so as colunas relevantes
pro dashboard, criando a coluna "ano_mes". Nao agrega nada aqui -- mantem
uma linha por coleta, igual veio da Silver, so mais enxuta. Quem agrega
(media, minimo, maximo etc.) e a camada DuckDB, via SQL, na hora que o
dashboard consulta.
"""

from pathlib import Path

import pandas as pd

SILVER_DIR = Path("data_lake/silver")
GOLD_DIR = Path("data_lake/gold")

COLUNAS_GOLD = [
     "estado_sigla",
     "regiao_sigla",
     "municipio",
     "produto",
     "bandeira",
     "data_coleta",
     "valor_venda",]


def gerar_gold(nome_arquivo: str) -> Path:
     """Le o Parquet da Silver, seleciona colunas relevantes e cria ano_mes."""
     caminho_silver = SILVER_DIR / nome_arquivo
     if not caminho_silver.exists():
         raise FileNotFoundError(f"Arquivo Silver nao encontrado: {caminho_silver}. Rode scripts/silver.py primeiro.")

     df = pd.read_parquet(caminho_silver)
     df = df[COLUNAS_GOLD].copy()
     df["ano_mes"] = df["data_coleta"].dt.to_period("M").astype(str)

     GOLD_DIR.mkdir(parents=True, exist_ok=True)
     destino = GOLD_DIR / nome_arquivo
     df.to_parquet(destino, index=False)
     return destino


if __name__ == "__main__":
     caminho = gerar_gold("preco_primeiro_semestre_2026.parquet")
     print(f"Gold gerada em: {caminho}")
