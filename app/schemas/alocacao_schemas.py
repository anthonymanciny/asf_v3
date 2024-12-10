from pydantic import BaseModel
from datetime import datetime


class AlocacaoBase(BaseModel):
    id_evento: int
    id_instituicao: int
    id_espaco_instituicao: int
    datahora: datetime
    status: int
    responsavel_local: str

    class Config:
        orm_mode = True


class AlocacaoCreate(AlocacaoBase):
    pass


class AlocacaoUpdate(AlocacaoBase):
    pass


class AlocacaoResponse(AlocacaoBase):
    id_alocacao: int

    class Config:
        orm_mode = True
