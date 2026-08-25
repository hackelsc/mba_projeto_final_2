"""
Arquivo que o Dagster le pra saber o que existe no projeto.
Rodar (a partir da raiz do projeto): dagster dev -f dagster_project/definitions.py
Abre a interface visual em http://localhost:3000
"""

import sys
from pathlib import Path

# Garante que a raiz do projeto (onde fica scripts/) e esta pasta (onde fica
# assets/) sejam encontradas nos imports, nao importa de onde o "dagster dev"
# for chamado.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from dagster import Definitions, load_assets_from_modules

from assets import bronze, duckdb, gold, silver

all_assets = load_assets_from_modules([bronze, silver, gold, duckdb])

defs = Definitions(assets=all_assets)
