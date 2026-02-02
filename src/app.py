import os
import sys
import streamlit as st

# Garantir que a raiz do projeto esteja no sys.path para permitir imports absolutos
ROOT = os.path.dirname(os.path.dirname(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Importações como pacote absoluto `src` — funciona tanto com
# `python -m src.app` quanto com `streamlit run src/app.py` quando
# a raiz do projeto estiver no `PYTHONPATH` ou adicionada acima.
from src.config import PAGE_CONFIG
from src.data_loader import get_filtered_data
from src.filters import render_filters, apply_filters
from src.metrics import calculate_metrics, display_metrics
from src.charts import display_all_charts

# --- Configuração da página ---
st.set_page_config(**PAGE_CONFIG)

# --- Carregamento dos dados ---
df = get_filtered_data()

if df is None:
    st.error("Não foi possível carregar os dados. Verifique a URL e tente novamente.")
    st.stop()

# --- Barra Lateral (Filtros) ---
filters = render_filters(df)
df_filtrado = apply_filters(df, filters)

# --- Conteudo principal ---
st.title("Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtos à esquerda para refinar sua análise.")

# --- Métricas Principais (KPIs) ---
metrics = calculate_metrics(df_filtrado)
display_metrics(metrics)

st.markdown("---")

# --- Análises Visuais com Plotly ---
display_all_charts(df_filtrado)

# --- Tabela de Dados Detalhados ---
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado)

# --- Rodapé ---
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 20px; color: #666;">
        <p><b>Desenvolvido por: Mathews Moura</b></p>
        <p>
            <a href="https://github.com/Mathewsmoura" target="_blank">GitHub</a> | 
            <a href="https://www.linkedin.com/in/mathews-moura/" target="_blank">LinkedIn</a>
        </p>
    </div>
""", unsafe_allow_html=True)
