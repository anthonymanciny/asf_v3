from sqlalchemy.orm import Session
from app.repositories.espacoinstituicao_repository import EspacoInstituicaoRepository
from app.schemas.espacaoinstituicao_schemas import EspacoInstituicaoCreate, EspacoInstituicaoUpdate


class EspacoInstituicaoService:
    def __init__(self, db_session: Session):
        self.repository = EspacoInstituicaoRepository(db_session)

    def create_espaco_instituicao(self, espaco_instituicao_data: EspacoInstituicaoCreate):
        return self.repository.create(espaco_instituicao_data)

    def get_espaco_instituicao(self, espaco_instituicao_id: int):
        return self.repository.get_by_id(espaco_instituicao_id)

    def update_espaco_instituicao(self, espaco_instituicao_id: int, espaco_instituicao_data: EspacoInstituicaoUpdate):
        return self.repository.update(espaco_instituicao_id, espaco_instituicao_data)

    def delete_espaco_instituicao(self, espaco_instituicao_id: int):
        return self.repository.delete(espaco_instituicao_id)

    def list_espacos_instituicoes(self):
        return self.repository.list_all()
