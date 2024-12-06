from pydantic import BaseModel
from typing import Optional

class InstituicaoBase(BaseModel):
    nome: str
    email: str
    endereco: str
    telefone: str
    observacao: Optional[str] = None

    class Config:
        orm_mode = True


class InstituicaoCreate(InstituicaoBase):
    pass


class InstituicaoUpdate(InstituicaoBase):
    pass


class InstituicaoResponse(InstituicaoBase):
    id_instituicao: int

    class Config:
        orm_mode = True
