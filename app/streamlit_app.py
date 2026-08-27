"""
Dashboard final: conecta no banco DuckDB gerado pela camada Gold e monta os
6 graficos combinados definidos para o projeto. Toda agregacao (media,
minimo, maximo, desvio padrao) acontece aqui via SQL -- a tabela
gold_combustiveis nao vem agregada.
"""

from pathlib import Path

import duckdb
import pandas as pd
import streamlit as st

DUCKDB_PATH = Path(__file__).resolve().parent.parent / "data_lake/duckdb/combustiveis.duckdb"

st.set_page_config(page_title="Precos de Combustiveis - 1o Semestre 2026", layout="wide")


@st.cache_resource
def conectar():
    if not DUCKDB_PATH.exists():
        st.error(f"Banco nao encontrado: {DUCKDB_PATH}. Rode scripts/camada_duckdb.py primeiro.")
        st.stop()
    return duckdb.connect(str(DUCKDB_PATH), read_only=True)


@st.cache_data
def listar_produtos(_con) -> list[str]:
    return _con.sql("SELECT DISTINCT produto FROM gold_combustiveis ORDER BY produto").df()["produto"].tolist()


@st.cache_data
def ranking_por_estado(_con, produto: str) -> pd.DataFrame:
    return _con.execute(
        """
        SELECT estado_sigla, AVG(valor_venda) AS preco_medio
        FROM gold_combustiveis
        WHERE produto = ?
        GROUP BY estado_sigla
        ORDER BY preco_medio DESC
        """,
        [produto],
    ).df()


@st.cache_data
def etanol_vs_gasolina(_con) -> pd.DataFrame:
    return _con.sql(
        """
        SELECT ano_mes, produto, AVG(valor_venda) AS preco_medio
        FROM gold_combustiveis
        WHERE produto IN ('ETANOL', 'GASOLINA')
        GROUP BY ano_mes, produto
        ORDER BY ano_mes
        """
    ).df()


@st.cache_data
def evolucao_no_tempo(_con, produto: str) -> pd.DataFrame:
    return _con.execute(
        """
        SELECT ano_mes, AVG(valor_venda) AS preco_medio
        FROM gold_combustiveis
        WHERE produto = ?
        GROUP BY ano_mes
        ORDER BY ano_mes
        """,
        [produto],
    ).df()


@st.cache_data
def diferenca_por_bandeira(_con, produto: str) -> pd.DataFrame:
    return _con.execute(
        """
        SELECT bandeira, AVG(valor_venda) AS preco_medio, COUNT(*) AS coletas
        FROM gold_combustiveis
        WHERE produto = ?
        GROUP BY bandeira
        HAVING COUNT(*) >= 30
        ORDER BY preco_medio DESC
        LIMIT 15
        """,
        [produto],
    ).df()


@st.cache_data
def dispersao_por_estado(_con, produto: str) -> pd.DataFrame:
    return _con.execute(
        """
        SELECT estado_sigla,
               AVG(valor_venda) AS preco_medio,
               MIN(valor_venda) AS preco_minimo,
               MAX(valor_venda) AS preco_maximo,
               STDDEV(valor_venda) AS desvio_padrao
        FROM gold_combustiveis
        WHERE produto = ?
        GROUP BY estado_sigla
        ORDER BY desvio_padrao DESC
        """,
        [produto],
    ).df()


@st.cache_data
def ranking_final(_con, produto: str, n: int = 5) -> pd.DataFrame:
    return _con.execute(
        """
        SELECT estado_sigla, AVG(valor_venda) AS preco_medio
        FROM gold_combustiveis
        WHERE produto = ?
        GROUP BY estado_sigla
        ORDER BY preco_medio ASC
        """,
        [produto],
    ).df()


con = conectar()
produtos = listar_produtos(con)

st.title("Precos de Combustiveis - 1o Semestre 2026")
st.caption("Fonte: Levantamento de Precos de Combustiveis (ANP) | Camadas Bronze -> Silver -> Gold -> DuckDB")

produto_selecionado = st.sidebar.selectbox(
    "Produto", produtos, index=produtos.index("GASOLINA") if "GASOLINA" in produtos else 0
)

st.header("1. Ranking de preco medio por estado")
df_ranking = ranking_por_estado(con, produto_selecionado)
st.bar_chart(df_ranking, x="estado_sigla", y="preco_medio")

st.header("2. Etanol vs Gasolina - evolucao mensal do preco medio")
df_etanol_gasolina = etanol_vs_gasolina(con)
tabela_comparativo = df_etanol_gasolina.pivot(index="ano_mes", columns="produto", values="preco_medio")
st.line_chart(tabela_comparativo)
if "ETANOL" in tabela_comparativo.columns and "GASOLINA" in tabela_comparativo.columns:
    razao = (tabela_comparativo["ETANOL"] / tabela_comparativo["GASOLINA"]).mean()
    st.metric("Razao media Etanol/Gasolina", f"{razao:.0%}", help="Regra pratica: etanol compensa abaixo de 70%")

st.header("3. Evolucao do preco no tempo")
df_evolucao = evolucao_no_tempo(con, produto_selecionado)
st.line_chart(df_evolucao, x="ano_mes", y="preco_medio")

st.header("4. Diferenca de preco por bandeira")
df_bandeira = diferenca_por_bandeira(con, produto_selecionado)
st.bar_chart(df_bandeira, x="bandeira", y="preco_medio")

st.header("5. Dispersao de precos por estado")
df_dispersao = dispersao_por_estado(con, produto_selecionado)
st.bar_chart(df_dispersao, x="estado_sigla", y="desvio_padrao")
with st.expander("Ver minimo, medio e maximo por estado"):
    st.dataframe(df_dispersao, use_container_width=True)

st.header("6. Ranking final - estados mais baratos")
df_final = ranking_final(con, produto_selecionado)
col_baratos, col_caros = st.columns(2)
with col_baratos:
    st.subheader("Top 5 mais baratos")
    st.dataframe(df_final.head(5), use_container_width=True)
with col_caros:
    st.subheader("Top 5 mais caros")
    st.dataframe(df_final.tail(5).sort_values("preco_medio", ascending=False), use_container_width=True)
