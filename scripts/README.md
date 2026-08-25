# scripts

Lógica real de transformação de cada camada do pipeline, em Python puro — sem
depender do Dagster. Cada camada em um arquivo separado, um por pessoa do
grupo, pra evitar conflito de edição no Git:

- `bronze.py` — lê o CSV de `source_data/`, renomeia colunas, salva Parquet em `data_lake/bronze/` (Pessoa 1).
- `silver.py` — lê a Bronze, limpa e tipa, salva em `data_lake/silver/` (Pessoa 2).
- `gold.py` — lê a Silver, seleciona colunas relevantes e cria `ano_mes`, salva em
  `data_lake/gold/` (Pessoa 3). Não agrega nada.
- `camada_duckdb.py` — lê a Gold e carrega numa tabela dentro de
  `data_lake/duckdb/combustiveis.duckdb` (Pessoa 3). A agregação (média,
  mínimo, máximo etc.) acontece via SQL, depois, nas queries do dashboard —
  não aqui.

Cada arquivo pode ser testado sozinho (`python scripts/bronze.py`), sem precisar
do Dagster rodando. Os arquivos em `dagster_project/assets/` só chamam essas
funções na ordem certa.
