# data_lake/bronze

Dados técnicos em Parquet, gerados pelo `scripts/bronze.py` a partir do CSV em
`source_data/`. Só renomeia as colunas do CSV original para snake_case
(ex: `Municipio` → `municipio`) — ainda sem limpeza de valores, tipos ou remoção
de duplicatas (isso é trabalho da Silver).

Gerado automaticamente. Não editar manualmente.
