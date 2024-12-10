from sqlalchemy.orm import Session
from app.models.models import Participacao
from app.schemas.participacao_schemas import ParticipacaoCreate, ParticipacaoUpdate


class ParticipacaoRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, participacao_data: ParticipacaoCreate) -> Participacao:
        participacao = Participacao(**participacao_data.dict())
        self.db_session.add(participacao)
        self.db_session.commit()
        self.db_session.refresh(participacao)
        return participacao

    def get_by_id(self, id_participacao: int) -> Participacao:
        return self.db_session.query(Participacao).filter_by(id_participacao=id_participacao).first()

    def update(self, id_participacao: int, participacao_data: ParticipacaoUpdate) -> Participacao:
        participacao = self.get_by_id(id_participacao)
        if participacao:
            for key, value in participacao_data.dict(exclude_unset=True).items():
                setattr(participacao, key, value)
            self.db_session.commit()
            self.db_session.refresh(participacao)
        return participacao

    def delete(self, id_participacao: int):
        participacao = self.get_by_id(id_participacao)
        if participacao:
            self.db_session.delete(participacao)
            self.db_session.commit()
        return participacao

    def list_all(self):
        return self.db_session.query(Participacao).all()
