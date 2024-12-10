docker-compose run app sh -c 'alembic init migrations'



remover containers
= docker rm $(docker ps -aq)
