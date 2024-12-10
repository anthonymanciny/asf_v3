from fastapi import APIRouter
from app.routes.alocacao_router import alocacao_router
from app.routes.espacoinstituicao_router import espaco_instituicao_router
from app.routes.evento_router import evento_router
from app.routes.instituicao_router import instituticao_router
from app.routes.participacao_router import participacao_router
from app.routes.pessoa_router import pessoa_router
from app.routes.auth_router import auth_router

# Criação de um roteador principal
api_router = APIRouter()

# Registro das rotas no roteador principal
api_router.include_router(alocacao_router)
api_router.include_router(espaco_instituicao_router)
api_router.include_router(evento_router)
api_router.include_router(instituticao_router)
api_router.include_router(participacao_router)
api_router.include_router(pessoa_router)

api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])