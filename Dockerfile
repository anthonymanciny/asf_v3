# Use a versão correta do Python
FROM python:3.12-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH="/"

# Copie os arquivos necessários para o Poetry
COPY ./poetry.lock /poetry.lock
COPY ./pyproject.toml /pyproject.toml

# Instale dependências do sistema e configure o Poetry
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends curl build-essential libpq-dev && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi && \
    apt-get remove -y curl && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /root/.cache

# Copie o código da aplicação
COPY ./app /app

# Defina o diretório de trabalho da aplicação
WORKDIR /app

# Exponha a porta que a aplicação vai rodar
EXPOSE 8000

