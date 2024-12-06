from pydantic import BaseModel

class ParticipacaoBase(BaseModel):
    id_evento: int
    id_pessoa: int
    tipo_participacao: str  # Pode ser 'P' (Participante) ou 'O' (Organizador), etc.

    class Config:
        orm_mode = True


class ParticipacaoCreate(ParticipacaoBase):
    pass


class ParticipacaoUpdate(ParticipacaoBase):
    pass


class ParticipacaoResponse(ParticipacaoBase):
    id_participacao: int

    class Config:
        orm_mode = True
