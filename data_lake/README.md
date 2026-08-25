# data_lake

Estrutura de pastas locais que representa o data lake do projeto, organizada por
camada (arquitetura em medalhão). Não usa um serviço de object storage dedicado
(tipo MinIO/S3) — é uma versão simplificada, adequada ao escopo do desafio, onde
cada camada é simplesmente uma pasta com arquivos.

- `bronze/` — dados técnicos em Parquet, colunas renomeadas, ainda sem limpeza.
- `silver/` — dados limpos, tipados e consolidados.
- `gold/` — dado limpo e enxuto (colunas relevantes + `ano_mes`), sem agregação.
- `duckdb/` — banco DuckDB com a Gold carregada; é aqui que a agregação
  (média, mínimo, máximo etc.) acontece, via SQL, na hora que o dashboard
  consulta os dados.

Nenhum arquivo de dado gerado aqui é versionado no Git (ver `.gitignore`) — cada
pessoa gera a própria cópia local rodando os scripts.
