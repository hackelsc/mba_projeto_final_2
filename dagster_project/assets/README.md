# dagster_project/assets

Um arquivo por camada, cada um "embrulhando" a função correspondente de
`scripts/` como um asset do Dagster. A dependência entre camadas é inferida
pelo nome do parâmetro bater com o nome do asset anterior (ex:
`bronze_combustiveis(raw_combustiveis: str)` depende de `raw_combustiveis`).

- `raw.py` — asset `raw_combustiveis` (Pessoa 1).
- `bronze.py` — asset `bronze_combustiveis` (Pessoa 1).
- `silver.py` — asset `silver_combustiveis`, a implementar (Pessoa 2).
- `gold.py` — asset `gold_combustiveis`, a ativar (Pessoa 3).
- `duckdb.py` — asset `duckdb_combustiveis`, a ativar (Pessoa 3).

Estes arquivos não devem conter lógica de transformação — só chamar a função
correspondente em `scripts/` e registrar metadados de saída.
