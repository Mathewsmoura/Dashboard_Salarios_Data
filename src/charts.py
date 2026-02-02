# --- Funções de Gráficos ---

import streamlit as st
import plotly.express as px
from .config import CHART_CONFIG, CHART_COLOR_SCALE


def plot_top_cargos(df_filtrado):
    """
    Exibe gráfico de top cargos por salário médio.
    
    Args:
        df_filtrado: DataFrame filtrado
    """
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(
            CHART_CONFIG['top_cargos_count']
        ).sort_values(ascending=True).reset_index()
        
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title="Top 10 cargos por salário médio",
            labels={'usd': 'Média salarial anual (USD)', 'cargo': ''}    
        )
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")


def plot_salary_distribution(df_filtrado):
    """
    Exibe gráfico de distribuição de salários.
    
    Args:
        df_filtrado: DataFrame filtrado
    """
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=CHART_CONFIG['histogram_bins'],
            title="Distribuição de salários anuais",
            labels={'usd': 'Faixa salarial (USD)', 'count': ''}
        )
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")


def plot_work_type_distribution(df_filtrado):
    """
    Exibe gráfico pizza de tipos de trabalho.
    
    Args:
        df_filtrado: DataFrame filtrado
    """
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole=0.5
        )
        grafico_remoto.update_traces(textinfo='percent+label')
        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")


def plot_data_scientist_by_country(df_filtrado):
    """
    Exibe gráfico de mapa coroplético com salário de Data Scientists por país.
    
    Args:
        df_filtrado: DataFrame filtrado
    """
    if not df_filtrado.empty:
        df_ds = df_filtrado[df_filtrado['cargo'] == 'Data Scientist']
        
        if not df_ds.empty:
            media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
            
            grafico_paises = px.choropleth(
                media_ds_pais,
                locations='residencia_iso3',
                color='usd',
                color_continuous_scale=CHART_COLOR_SCALE,
                title='Salário médio de Cientista de Dados por país',
                labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'}
            )
            grafico_paises.update_layout(title_x=0.1)
            st.plotly_chart(grafico_paises, use_container_width=True)
        else:
            st.warning("Nenhum dado de Data Scientist para exibir no gráfico de países.")
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")


def display_all_charts(df_filtrado):
    """
    Exibe todos os gráficos organizados em colunas.
    
    Args:
        df_filtrado: DataFrame filtrado
    """
    st.subheader("Gráficos")
    
    col_graf1, col_graf2 = st.columns(2)
    
    with col_graf1:
        plot_top_cargos(df_filtrado)
    
    with col_graf2:
        plot_salary_distribution(df_filtrado)
    
    col_graf3, col_graf4 = st.columns(2)
    
    with col_graf3:
        plot_work_type_distribution(df_filtrado)
    
    with col_graf4:
        plot_data_scientist_by_country(df_filtrado)
