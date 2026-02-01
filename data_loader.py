# --- Carregamento de Dados com Cache ---

import streamlit as st
import pandas as pd
from config import DATA_URL


@st.cache_data
def load_data():
    """
    Carrega os dados da URL com cache automático.
    O cache é mantido enquanto o app está rodando.
    """
    try:
        df = pd.read_csv(DATA_URL)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar dados: {str(e)}")
        return None


def get_filtered_data():
    """
    Retorna o DataFrame carregado com cache.
    """
    return load_data()
