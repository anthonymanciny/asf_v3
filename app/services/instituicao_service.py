from sqlalchemy.orm import Session
from app.repositories.instituicao_repository import InstituicaoRepository
from app.schemas.instituicao_schemas import InstituicaoCreate, InstituicaoUpdate


class InstituicaoService:
    def __init__(self, db_session: Session):
        self.repository = InstituicaoRepository(db_session)

    def create_instituicao(self, instituicao_data: InstituicaoCreate):
        return self.repository.create(instituicao_data)

    def get_instituicao(self, instituicao_id: int):
        return self.repository.get_by_id(instituicao_id)

    def update_instituicao(self, instituicao_id: int, instituicao_data: InstituicaoUpdate):
        return self.repository.update(instituicao_id, instituicao_data)

    def delete_instituicao(self, instituicao_id: int):
        return self.repository.delete(instituicao_id)

    def list_instituicoes(self):
        return self.repository.list_all()
