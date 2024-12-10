from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date


class Instituicao(BaseModel):
    id: int
    nome: str
    email: str
    endereco: str
    telefone: str
    obs: str

    class Config:
        orm_mode = True

class Pessoa(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str
    cpf: str
    data_nascimento: Optional[date] = None
    genero : str
    
    class Config:
        orm_mode = True

class Evento(BaseModel):
    id: int
    nome: str
    datahora: datetime
    responsavel_evento: str


    class Config:
        orm_mode = True

class Participacao(BaseModel):
    id: int

    id_evento: int
    evento: Evento

    id_pessoa: int
    pessoa: Pessoa

    tipo: str

    class Config:
        orm_mode = True

class EspacoInstituicao(BaseModel):
    id: int
    
    id_instituicao: int
    instituicao: Instituicao
    nome: str
    capacidade: int
    responsavel: str

    class Config:
        orm_mode = True



class Alocacao(BaseModel):
    id: int

    id_evento: int
    evento: Evento

    id_instituicao_cedente: int
    instituicao_cedente: Instituicao

    id_espaco: int
    espaco: EspacoInstituicao

    datahora : datetime
    status : str
    responsavel_local: str 

    class Config:
        orm_mode = True

