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

    def get_by_id(self, participacao_id: int) -> Participacao:
        return self.db_session.query(Participacao).filter_by(participacao_id=participacao_id).first()

    def update(self, participacao_id: int, participacao_data: ParticipacaoUpdate) -> Participacao:
        participacao = self.get_by_id(participacao_id)
        if participacao:
            for key, value in participacao_data.dict(exclude_unset=True).items():
                setattr(participacao, key, value)
            self.db_session.commit()
            self.db_session.refresh(participacao)
        return participacao

    def delete(self, participacao_id: int):
        participacao = self.get_by_id(participacao_id)
        if participacao:
            self.db_session.delete(participacao)
            self.db_session.commit()
        return participacao

    def list_all(self):
        return self.db_session.query(Participacao).all()
