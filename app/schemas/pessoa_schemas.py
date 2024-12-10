from pydantic import BaseModel
from typing import Optional
from datetime import date

# Base para criar e validar entradas no sistema
class PessoaBase(BaseModel):
    nome: str
    email: str
    celular: str
    telefone: Optional[str] = None
    cpf: str
    data_nascimento: date
    genero: Optional[str] = None

    class Config:
        orm_mode = True


# Modelo para criação de uma nova pessoa
class PessoaCreate(PessoaBase):
    senha: str  # Senha recebida no backend para hashing


# Modelo para atualização (permite mudanças parciais ou completas)
class PessoaUpdate(PessoaBase):
    pass


# Esquema para login (apenas email e senha)
class LoginSchema(BaseModel):
    email: str
    senha: str


# Modelo para tokens de autenticação
class Token(BaseModel):
    access_token: str
    token_type: str


# Dados contidos no token (útil para dependências)
class TokenData(BaseModel):
    username: Optional[str] = None


# Modelo de resposta com informações completas (incluindo ID)
class PessoaResponse(PessoaBase):
    id_pessoa: int

    class Config:
        orm_mode = True
