"""
Camada Silver: le o Parquet da Bronze, aplica limpeza e padronizacao dos
dados e salva como Parquet em data_lake/silver/. Baseado nas conclusoes da
analise exploratoria:
- Converte "data_coleta" (texto dd/mm/aaaa) para tipo data.
- Converte "valor_venda" (texto com virgula decimal) para numero.
- Remove linhas duplicadas (erro de coleta confirmado).
- Descarta "valor_compra" (coluna 100% vazia).
- Padroniza colunas de texto com strip() (espacos extras, ex: cnpj_revenda).
"""

from pathlib import Path

import pandas as pd

BRONZE_DIR = Path("data_lake/bronze")
SILVER_DIR = Path("data_lake/silver")


def gerar_silver(nome_arquivo: str) -> Path:
    """Le o Parquet da Bronze, limpa e padroniza os dados, salva na Silver."""
    caminho_bronze = BRONZE_DIR / nome_arquivo
    if not caminho_bronze.exists():
        raise FileNotFoundError(f"Arquivo Bronze nao encontrado: {caminho_bronze}. Rode scripts/bronze.py primeiro.")

    df = pd.read_parquet(caminho_bronze)

    df = df.drop_duplicates()

    df = df.drop(columns=["valor_compra"])

    df["data_coleta"] = pd.to_datetime(df["data_coleta"], format="%d/%m/%Y")
    df["valor_venda"] = df["valor_venda"].str.replace(",", ".", regex=False).astype(float)

    colunas_texto = df.select_dtypes(include="string").columns
    for coluna in colunas_texto:
        df[coluna] = df[coluna].str.strip()

    SILVER_DIR.mkdir(parents=True, exist_ok=True)
    destino = SILVER_DIR / nome_arquivo
    df.to_parquet(destino, index=False)
    return destino


if __name__ == "__main__":
    caminho = gerar_silver("preco_primeiro_semestre_2026.parquet")
    print(f"Silver gerada em: {caminho}")
