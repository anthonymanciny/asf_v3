from sqlalchemy.orm import Session
from app.repositories.participacao_repository import ParticipacaoRepository
from app.schemas.participacao_schemas import ParticipacaoCreate, ParticipacaoUpdate


class ParticipacaoService:
    def __init__(self, db_session: Session):
        self.repository = ParticipacaoRepository(db_session)

    def create_participacao(self, participacao_data: ParticipacaoCreate):
        return self.repository.create(participacao_data)

    def get_participacao(self, id_participacao: int):
        return self.repository.get_by_id(id_participacao)

    def update_participacao(self, id_participacao: int, participacao_data: ParticipacaoUpdate):
        return self.repository.update(id_participacao, participacao_data)

    def delete_participacao(self, id_participacao: int):
        return self.repository.delete(id_participacao)

    def list_participacoes(self):
        return self.repository.list_all()
