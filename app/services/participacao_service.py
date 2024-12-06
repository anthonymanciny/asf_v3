from sqlalchemy.orm import Session
from app.repositories.participacao_repository import ParticipacaoRepository
from app.schemas.participacao_schemas import ParticipacaoCreate, ParticipacaoUpdate


class ParticipacaoService:
    def __init__(self, db_session: Session):
        self.repository = ParticipacaoRepository(db_session)

    def create_participacao(self, participacao_data: ParticipacaoCreate):
        return self.repository.create(participacao_data)

    def get_participacao(self, participacao_id: int):
        return self.repository.get_by_id(participacao_id)

    def update_participacao(self, participacao_id: int, participacao_data: ParticipacaoUpdate):
        return self.repository.update(participacao_id, participacao_data)

    def delete_participacao(self, participacao_id: int):
        return self.repository.delete(participacao_id)

    def list_participacoes(self):
        return self.repository.list_all()
