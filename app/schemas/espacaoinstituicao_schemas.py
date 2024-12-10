from pydantic import BaseModel

class EspacoInstituicaoBase(BaseModel):
    id_instituicao: int
    nome_espaco: str
    capacidade: int
    responsavel: str

    class Config:
        orm_mode = True


class EspacoInstituicaoCreate(EspacoInstituicaoBase):
    pass


class EspacoInstituicaoUpdate(EspacoInstituicaoBase):
    pass


class EspacoInstituicaoResponse(EspacoInstituicaoBase):
    id_espaco_instituicao: int

    class Config:
        orm_mode = True
