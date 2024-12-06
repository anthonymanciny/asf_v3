from app.routes.aapp_router import api_router
# from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


app = FastAPI()





@app.get('/')
def root():
    return "teste do bichao"


@app.get('/docker')
def root():
    return "eu sou o docker"

app.include_router(api_router)