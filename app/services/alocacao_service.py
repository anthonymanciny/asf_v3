from sqlalchemy.orm import Session
from app.repositories.alocacao_repository import AlocacaoRepository
from app.schemas.alocacao_schemas import AlocacaoCreate, AlocacaoUpdate


class AlocacaoService:
    def __init__(self, db_session: Session):
        self.repository = AlocacaoRepository(db_session)

    def create_alocacao(self, alocacao_data: AlocacaoCreate):
        return self.repository.create(alocacao_data)

    def get_alocacao(self, alocacao_id: int):
        return self.repository.get_by_id(alocacao_id)

    def update_alocacao(self, alocacao_id: int, alocacao_data: AlocacaoUpdate):
        return self.repository.update(alocacao_id, alocacao_data)

    def delete_alocacao(self, alocacao_id: int):
        return self.repository.delete(alocacao_id)

    def list_alocacoes(self):
        return self.repository.list_all()
