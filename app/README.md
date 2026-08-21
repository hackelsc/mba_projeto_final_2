# app

Dashboard final em Streamlit (Pessoa 3). Consulta a tabela `gold_combustiveis`
dentro do banco em `data_lake/duckdb/combustiveis.duckdb` usando SQL — é
aqui que a agregação (média, mínimo, máximo, desvio padrão por
estado/mês/produto/bandeira) acontece, via `GROUP BY`. A tabela em si não
vem agregada; cada gráfico faz sua própria consulta SQL conforme a
pergunta que precisa responder.

Para rodar: `streamlit run app/streamlit_app.py`
