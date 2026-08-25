# data_lake/gold

Tabela limpa e enxuta, gerada por `scripts/gold.py` (Pessoa 3) a partir do
que está em `data_lake/silver/`. Mantém uma linha por coleta (mesma
granularidade da Silver), só com as colunas relevantes: `estado_sigla`,
`regiao_sigla`, `municipio`, `produto`, `bandeira`, `data_coleta`, `ano_mes`
e `valor_venda`.

Não faz agregação nenhuma — isso é responsabilidade da camada DuckDB, via
SQL, na hora que o dashboard consulta os dados.

Gerado automaticamente. Não editar manualmente.
