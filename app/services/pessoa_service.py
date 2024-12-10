from sqlalchemy.orm import Session
from app.repositories.pessoa_repository import PessoaRepository
from app.schemas.pessoa_schemas import PessoaCreate, PessoaUpdate


class PessoaService:
    def __init__(self, db_session: Session):
        self.repository = PessoaRepository(db_session)

    def create_pessoa(self, pessoa_data: PessoaCreate):
        return self.repository.create(pessoa_data)

    def get_pessoa(self, pessoa_id: int):
        return self.repository.get_by_id(pessoa_id)

    def update_pessoa(self, pessoa_id: int, pessoa_data: PessoaUpdate):
        return self.repository.update(pessoa_id, pessoa_data)

    def delete_pessoa(self, pessoa_id: int):
        return self.repository.delete(pessoa_id)

    def list_pessoas(self):
        return self.repository.list_all()
