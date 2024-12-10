from app.routes.aapp_router import api_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


app = FastAPI()

# Configuração do CORS para permitir o frontend em localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Permitir somente o frontend Angular
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)




@app.get('/')
def root():
    return "teste do bichao"



app.include_router(api_router)