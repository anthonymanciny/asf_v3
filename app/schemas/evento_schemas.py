from pydantic import BaseModel
from enum import Enum



class EventoBase(BaseModel):
    nome_evento: str
    responsavel_evento: str
    status: int
    qnt_voluntarios:int

class EventoCreate(EventoBase):
    pass

class EventoUpdate(EventoBase):
    nome_evento: str | None = None
    responsavel_evento: str | None = None
    status: int | None = None

    class Config:
        orm_mode = True

class EventoResponse(EventoBase):
    id_evento: int