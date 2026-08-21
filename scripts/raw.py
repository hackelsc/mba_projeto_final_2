"""
Camada Raw: copia o CSV de source_data/ para data_lake/raw/, sem nenhuma
transformacao. Preserva o dado bruto como ponto de partida oficial do
pipeline, independente do arquivo original em source_data/ ser alterado
ou removido depois.
"""

import shutil
from pathlib import Path

SOURCE_DIR = Path("source_data")
RAW_DIR = Path("data_lake/raw")


def gerar_raw(nome_arquivo: str) -> Path:
    """Copia nome_arquivo de source_data/ para data_lake/raw/, criando a pasta se preciso."""
    origem = SOURCE_DIR / nome_arquivo
    if not origem.exists():
        raise FileNotFoundError(f"Arquivo fonte nao encontrado: {origem}")

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    destino = RAW_DIR / nome_arquivo
    shutil.copy(origem, destino)
    return destino


if __name__ == "__main__":
    caminho = gerar_raw("preco_primeiro_semestre_2026.csv")
    print(f"Raw gerada em: {caminho}")
