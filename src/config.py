# --- Configurações e Constantes ---

# URL dos dados
DATA_URL = "https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv"

# Configuração da página
PAGE_CONFIG = {
    "page_title": "Dashboard de Salários na Área de Dados",
    "page_icon": "📊",
    "layout": "wide",
}

# Colunas de filtros disponíveis
FILTER_COLUMNS = {
    "ano": "Ano",
    "senioridade": "Senioridade",
    "contrato": "Tipo de Contrato",
    "tamanho_empresa": "Tamanho da Empresa",
}

# Configurações de gráficos
CHART_CONFIG = {
    "top_cargos_count": 10,
    "histogram_bins": 30,
}

# Cores e estilos
CHART_COLOR_SCALE = "rdylgn"
