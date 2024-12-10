from sqlalchemy.orm import Session
from app.models.models import Instituicao
from app.schemas.instituicao_schemas import InstituicaoCreate, InstituicaoUpdate


class InstituicaoRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, instituicao_data: InstituicaoCreate) -> Instituicao:
        # Criar uma instância da Instituicao com base nos dados recebidos
        instituicao = Instituicao(**instituicao_data.dict())
        self.db_session.add(instituicao)
        self.db_session.commit()
        self.db_session.refresh(instituicao)
        return instituicao

    def get_by_id(self, instituicao_id: int) -> Instituicao:
        # Alterar para usar id_instituicao em vez de id
        return self.db_session.query(Instituicao).filter_by(id_instituicao=instituicao_id).first()

    def update(self, instituicao_id: int, instituicao_data: InstituicaoUpdate) -> Instituicao:
        # Buscar a instituicao pelo id_instituicao
        instituicao = self.get_by_id(instituicao_id)
        if instituicao:
            # Atualizar os campos da Instituicao com os dados fornecidos
            for key, value in instituicao_data.dict(exclude_unset=True).items():
                setattr(instituicao, key, value)
            self.db_session.commit()
            self.db_session.refresh(instituicao)
        return instituicao

    def delete(self, instituicao_id: int):
        # Buscar a instituicao pelo id_instituicao
        instituicao = self.get_by_id(instituicao_id)
        if instituicao:
            self.db_session.delete(instituicao)
            self.db_session.commit()
        return instituicao

    def list_all(self):
        # Retornar todas as instituicoes
        return self.db_session.query(Instituicao).all()
