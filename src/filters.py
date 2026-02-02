# --- Lógica de Filtros ---

import streamlit as st
from .config import FILTER_COLUMNS


def render_filters(df):
    """
    Renderiza os filtros na sidebar e retorna os valores selecionados.
    
    Args:
        df: DataFrame com os dados
        
    Returns:
        dict: Dicionário com as seleções de cada filtro
    """
    st.sidebar.header("Filtros")
    
    filters = {}
    
    for column, label in FILTER_COLUMNS.items():
        values_disponiveis = sorted(df[column].unique())
        value_selecionado = st.sidebar.selectbox(
            label,
            options=["Todos"] + list(values_disponiveis),
            index=0,
            key=f"filter_{column}"
        )
        
        # Converte seleção em lista para manter compatibilidade
        if value_selecionado == "Todos":
            filters[column] = values_disponiveis
        else:
            filters[column] = [value_selecionado]
    
    return filters


def apply_filters(df, filters):
    """
    Aplica os filtros selecionados ao DataFrame.
    
    Args:
        df: DataFrame original
        filters: Dicionário com as seleções de filtros
        
    Returns:
        DataFrame filtrado
    """
    df_filtrado = df[
        (df['ano'].isin(filters.get('ano', df['ano'].unique()))) &
        (df['senioridade'].isin(filters.get('senioridade', df['senioridade'].unique()))) &
        (df['contrato'].isin(filters.get('contrato', df['contrato'].unique()))) &
        (df['tamanho_empresa'].isin(filters.get('tamanho_empresa', df['tamanho_empresa'].unique())))
    ]
    
    return df_filtrado
