import pandas as pd
from src.filters import apply_filters

def test_apply_filters_multiple_selection():
    """Testa se a aplicação de filtros usando múltiplas seleções (ES-2) funciona adequadamente."""
    # Arrange
    data = {
        'ano': [2020, 2021, 2022, 2023],
        'senioridade': ['Junior', 'Mid', 'Senior', 'Senior'],
        'contrato': ['Full-time', 'Part-time', 'Contract', 'Full-time'],
        'tamanho_empresa': ['S', 'M', 'L', 'M']
    }
    df = pd.DataFrame(data)
    
    filters = {
        'ano': [2021, 2022, 2023],  # 3 específicos selecionados
        'senioridade': ['Mid', 'Senior'], # 2 Múltiplos selecionados 
        'contrato': ['Full-time', 'Part-time', 'Contract'], # Simulação de vazio convertida em "Todos"
        'tamanho_empresa': ['M', 'L'] 
    }
    
    # Act
    df_filtrado = apply_filters(df, filters)
    
    # Assert
    assert len(df_filtrado) == 3  # (2021, Mid, PT, M) | (2022, Sen, C, L) | (2023, Sen, FT, M)
    assert 'Junior' not in df_filtrado['senioridade'].values
    assert 2020 not in df_filtrado['ano'].values

def test_apply_filters_short_circuit_all_items():
    """Testa se a função retorna o DF intacto quando nenhum filtro real é aplicado (ES-4)."""
    # Arrange
    df = pd.DataFrame({
        'ano': [2021, 2022],
        'senioridade': ['Mid', 'Senior'],
        'contrato': ['Full-time', 'Contract'],
        'tamanho_empresa': ['M', 'L']
    })
    
    # Filtros preenchidos com gama inteira de possiveis
    filters_todos = {
        'ano': [2021, 2022],
        'senioridade': ['Mid', 'Senior'],
        'contrato': ['Full-time', 'Contract'],
        'tamanho_empresa': ['M', 'L']
    }
    
    # Act
    df_filtrado = apply_filters(df, filters_todos)
    
    # Assert
    assert len(df_filtrado) == 2
    assert id(df) == id(df_filtrado) # ID de mémoria deve bater, implicando no O(1) return
