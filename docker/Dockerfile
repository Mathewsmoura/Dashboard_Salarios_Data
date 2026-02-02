# Estágio 1: Builder — instala dependências
FROM python:3.11-slim as builder

# Impede que Python escreva arquivos .pyc e bufferize stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define diretório de trabalho
WORKDIR /app

# Copia requirements.txt
COPY requirements.txt /app/requirements.txt

# Instala dependências em diretório temporário (lib + bin)
RUN pip install --upgrade pip setuptools wheel && \
    pip install --target=/app/deps --no-cache-dir -r /app/requirements.txt

# Estágio 2: Runtime — imagem final otimizada
FROM python:3.11-slim as runtime

# Metadados
LABEL maintainer="Mathews Moura <https://github.com/Mathewsmoura>"

# Variáveis de ambiente — impede .pyc e bufferiza output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define diretório de trabalho
WORKDIR /app

# Instala curl para healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Cria usuário não-root para maior segurança
RUN groupadd --gid 1000 appuser && \
    useradd --uid 1000 --gid 1000 --create-home appuser

# Copia dependências do builder (lib + bin)
COPY --from=builder /app/deps /app/deps

# Adiciona os executáveis e bibliotecas ao PATH e PYTHONPATH
ENV PATH="/app/deps/bin:$PATH"
ENV PYTHONPATH="/app/deps:$PYTHONPATH"

# Copia código-fonte da aplicação
COPY . /app

# Garante que todos os arquivos pertencem ao usuário não-root
RUN chown -R appuser:appuser /app
USER appuser

# Variáveis de ambiente específicas do Streamlit
ENV STREAMLIT_SERVER_PORT=8000
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLECORS=false
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

EXPOSE 8000

# Healthcheck — verifica se a aplicação está respondendo (start-period maior para carregar dados)
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

# Entrypoint — executa a aplicação Streamlit
ENTRYPOINT ["streamlit", "run", "src/app.py"]
