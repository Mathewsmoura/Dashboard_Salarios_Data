# Dashboard de Salários na Área de Dados

Uma aplicação web interativa para análise e visualização de dados salariais na área de dados.

## 🛠️ Tecnologias Utilizadas

Projeto de visualização e análise de dados salariais na área de dados. Este dashboard foi desenvolvido como parte da **Imersão de Dados com Python** da Alura com algumas implementações de pipeline CI/CD com Docker-compose e GitHub Actions.

Principais funcionalidades:
- Filtros interativos por ano, senioridade, tipo de contrato e tamanho da empresa
- KPIs (salário médio, salário máximo, total de registros, cargo mais frequente)
- Gráficos interativos com Plotly (barras, histograma, pizza e mapa coroplético)
- Tabela de dados filtrados para consulta detalhada

Tecnologias utilizadas
- Python
- Streamlit
- Pandas
- Plotly

Como executar

### Opção 1: Local (Desenvolvimento)

1. Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Windows PowerShell
venv\Scripts\Activate.ps1
# ou cmd
venv\Scripts\activate.bat
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Execute o app:

```bash
streamlit run app.py
```

A aplicação estará acessível em `http://localhost:8501`

### Opção 2: Docker (Produção / CI-CD)

Tenha o Docker e Docker Compose instalados. Após clonar o repositório:

```bash
docker-compose up --build
```

A aplicação será automaticamente iniciada e estará acessível em `http://localhost:8501`

Para parar o container:

```bash
docker-compose down
```

Estrutura do projeto (resumida)
- `app.py` — orquestrador principal do dashboard
- `config.py` — constantes e configurações
- `data_loader.py` — carregamento e cache dos dados
- `filters.py` — lógica e aplicação de filtros
- `metrics.py` — cálculo e exibição de métricas (KPIs)
- `charts.py` — funções para geração dos gráficos
- `requirements.txt` — dependências do projeto
- `Dockerfile` — imagem Docker otimizada multi-stage
- `docker-compose.yml` — orquestração do container com healthcheck e limites de recursos
- `.github/workflows/build-and-publish.yml` — pipeline CI/CD (GitHub Actions)

Créditos
- Desenvolvido por: Mathews Moura através da Imersão de Dados com Python da Alura
- Site Alura: https://www.alura.com.br/
- GitHub: https://github.com/Mathewsmoura
- LinkedIn: https://www.linkedin.com/in/mathews-moura/

Licença
- Este repositório contém material criado como parte da Imersão de Dados com Python (Alura). Sinta-se livre para usar e adaptar o código para fins educacionais.

---

- **Pandas** (>=1.5, <3.0) - Manipulação e análise de dados
- **Streamlit** (>=1.20, <2.0) - Framework para criação de aplicações web
- **Plotly** (>=5.0, <6.0) - Visualizações interativas