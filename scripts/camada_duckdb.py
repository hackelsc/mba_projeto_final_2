"""
Camada DuckDB: carrega o Parquet da Gold dentro de um banco DuckDB, para que
o dashboard possa consultar os dados com SQL em vez de Pandas puro. Nao faz
nenhuma transformacao nova -- e so uma copia da Gold dentro de um banco.
"""

from pathlib import Path

import duckdb

GOLD_DIR = Path("data_lake/gold")
DUCKDB_DIR = Path("data_lake/duckdb")
NOME_BANCO = "combustiveis.duckdb"


def gerar_duckdb(nome_arquivo: str) -> Path:
    """Le o Parquet da Gold e carrega na tabela gold_combustiveis do DuckDB."""
    caminho_gold = GOLD_DIR / nome_arquivo
    if not caminho_gold.exists():
        raise FileNotFoundError(f"Arquivo Gold nao encontrado: {caminho_gold}. Rode scripts/gold.py primeiro.")

    DUCKDB_DIR.mkdir(parents=True, exist_ok=True)
    destino = DUCKDB_DIR / NOME_BANCO

    con = duckdb.connect(str(destino))
    con.sql(f"""
        CREATE OR REPLACE TABLE gold_combustiveis AS
        SELECT * FROM '{caminho_gold}'
    """)
    con.close()
    return destino


if __name__ == "__main__":
    caminho = gerar_duckdb("preco_primeiro_semestre_2026.parquet")
    print(f"Banco DuckDB gerado em: {caminho}")
