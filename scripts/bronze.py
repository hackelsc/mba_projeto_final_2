"""
Camada Bronze: le o CSV da camada Raw (data_lake/raw.py), renomeia colunas para snake_case
e salva como Parquet em data/bronze/. Ainda sem limpeza de valores
(isso e trabalho da Silver) -- so uma "traducao tecnica" do CSV bruto.
"""

from pathlib import Path

import pandas as pd

RAW_DIR = Path("data_lake/raw")
BRONZE_DIR = Path("data_lake/bronze")

# Nomes de coluna como vem no CSV oficial da ANP -> snake_case
COLUNAS_RENAME = {
    "Regiao - Sigla": "regiao_sigla",
    "Estado - Sigla": "estado_sigla",
    "Municipio": "municipio",
    "Revenda": "revenda",
    "CNPJ da Revenda": "cnpj_revenda",
    "Nome da Rua": "nome_rua",
    "Numero Rua": "numero_rua",
    "Complemento": "complemento",
    "Bairro": "bairro",
    "Cep": "cep",
    "Produto": "produto",
    "Data da Coleta": "data_coleta",
    "Valor de Venda": "valor_venda",
    "Valor de Compra": "valor_compra",
    "Unidade de Medida": "unidade_medida",
    "Bandeira": "bandeira",
}


def gerar_bronze(nome_arquivo: str) -> Path:
    """Le o CSV da Raw e salva como Parquet na Bronze, so renomeando colunas."""
    caminho_raw = RAW_DIR / nome_arquivo
    if not caminho_raw.exists():
        raise FileNotFoundError(f"Arquivo Raw nao encontrado: {caminho_raw}. Rode scripts/raw.py primeiro.")

    df = pd.read_csv(caminho_raw, sep=";", encoding="utf-8-sig", dtype="string")
    df = df.rename(columns=COLUNAS_RENAME)

    BRONZE_DIR.mkdir(parents=True, exist_ok=True)
    destino = BRONZE_DIR / nome_arquivo.replace(".csv", ".parquet")
    df.to_parquet(destino, index=False)
    return destino


if __name__ == "__main__":
    caminho = gerar_bronze("preco_primeiro_semestre_2026.csv")
    print(f"Bronze gerada em: {caminho}")
