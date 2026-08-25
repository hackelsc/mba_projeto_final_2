# data_lake/duckdb

Banco DuckDB (`combustiveis.duckdb`), gerado por `scripts/camada_duckdb.py`
(Pessoa 3) a partir da tabela em `data_lake/gold/`. Não tem transformação
própria — só carrega o Parquet da Gold (dado limpo, ainda não agregado)
dentro de uma tabela.

É aqui que a agregação (média, mínimo, máximo etc.) acontece de fato,
via SQL, na hora que o dashboard consulta os dados — não antes.

Gerado automaticamente. Não editar manualmente.
