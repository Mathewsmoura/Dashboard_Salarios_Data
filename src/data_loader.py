# --- Carregamento de Dados com Cache ---

import streamlit as st
import pandas as pd
from .config import DATA_URL, CSV_DTYPES


@st.cache_data(ttl=3600, show_spinner="Carregando dados...")
def load_data():
    """
    Carrega os dados da URL com cache automático.
    O cache expira após 1 hora (ttl=3600) e exibe spinner durante o carregamento.
    """
    try:
        df = pd.read_csv(DATA_URL, dtype=CSV_DTYPES)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {str(e)}")
        return None


def get_filtered_data():
    """
    Retorna o DataFrame carregado com cache.
    """
    return load_data()
