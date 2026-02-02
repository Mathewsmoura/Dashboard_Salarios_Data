# --- Cálculo de Métricas ---

import streamlit as st


def calculate_metrics(df_filtrado):
    """
    Calcula as métricas principais (KPIs) do dashboard.
    
    Args:
        df_filtrado: DataFrame filtrado
        
    Returns:
        dict: Dicionário com as métricas calculadas
    """
    metrics = {
        "salario_medio": 0,
        "salario_maximo": 0,
        "total_registros": 0,
        "cargo_mais_frequente": ""
    }
    
    if not df_filtrado.empty:
        metrics["salario_medio"] = df_filtrado['usd'].mean()
        metrics["salario_maximo"] = df_filtrado['usd'].max()
        metrics["total_registros"] = df_filtrado.shape[0]
        metrics["cargo_mais_frequente"] = df_filtrado['cargo'].mode()[0]
    
    return metrics


def display_metrics(metrics):
    """
    Exibe as métricas calculadas em colunas.
    
    Args:
        metrics: Dicionário com as métricas
    """
    st.subheader("Métricas gerais (Salário anual em USD)")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Salário médio", f"${metrics['salario_medio']:,.0f}")
    col2.metric("Salário máximo", f"${metrics['salario_maximo']:,.0f}")
    col3.metric("Total de registros", f"${metrics['total_registros']:,}")
    col4.metric("Cargo mais frequente", metrics['cargo_mais_frequente'])
