#!/bin/bash
# wait-for-it.sh
# Aguarda o serviço PostgreSQL ficar disponível antes de rodar o alembic

set -e

host="$1"
shift
port="$1"
shift

until nc -z "$host" "$port"; do
  echo "Aguardando o banco de dados $host:$port..."
  sleep 2
done

echo "Banco de dados $host:$port está disponível! Executando alembic upgrade..."
exec "$@"
