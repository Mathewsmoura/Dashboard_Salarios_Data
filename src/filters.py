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
        # Utiliza dropna() para contornar TypeErrors em caso de nulos (ES-2/QA Note)
        values_disponiveis = sorted(df[column].dropna().unique())
        
        valores_selecionados = st.sidebar.multiselect(
            label,
            options=list(values_disponiveis),
            default=[],
            placeholder="Selecione... (Vazio = Todos)",
            key=f"filter_{column}"
        )
        
        # Se vazio, consideramos que o analista deseja visualizar 'Todos' os dados
        if not valores_selecionados:
            filters[column] = values_disponiveis
        else:
            filters[column] = valores_selecionados
    
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
