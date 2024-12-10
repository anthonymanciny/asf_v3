from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_user
from app.db.depends import get_db
from app.models.models import Pessoa
from app.schemas.pessoa_schemas import PessoaBase
from app.schemas.validation import LoginSchema, Token
from app.auth.hashing import verify_password, get_password_hash
from app.auth.jwt import create_access_token
from datetime import timedelta

from decouple import config


ACCESS_TOKEN_EXPIRE_MINUTES = config('ACCESS_TOKEN_EXPIRE_MINUTES')



auth_router = APIRouter()

@auth_router.post("/login", response_model=Token)
def login(user: LoginSchema, db: Session = Depends(get_db)):
    pessoa = db.query(Pessoa).filter(Pessoa.email == user.email).first()
    if not pessoa or not verify_password(user.senha, pessoa.senha):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    
    access_token = create_access_token(data={"sub": pessoa.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@auth_router.get("/protected-route", response_model=PessoaBase)
def protected_route(current_user: PessoaBase = Depends(get_current_user)):
    return current_user



@auth_router.get("/profile", response_model=PessoaBase)
def read_profile(current_user: PessoaBase = Depends(get_current_user)):
    return current_user