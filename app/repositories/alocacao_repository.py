from sqlalchemy.orm import Session
from app.models.models import Alocacao
from app.schemas.alocacao_schemas import AlocacaoCreate, AlocacaoUpdate

class AlocacaoRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, alocacao_data: AlocacaoCreate) -> Alocacao:
        alocacao = Alocacao(**alocacao_data.dict()
            # id_evento=alocacao_data.id_evento,
            # id_instituicao=alocacao_data.id_instituicao,
            # id_espaco_instituicao=alocacao_data.id_espaco_instituicao,
            # datahora=alocacao_data.datahora,
            # status=alocacao_data.status,  # O valor já será passado corretamente
            # responsavel_local=alocacao_data.responsavel_local
        )
        
        self.db_session.add(alocacao)
        self.db_session.commit()
        self.db_session.refresh(alocacao)
        return alocacao

    def get_by_id(self, alocacao_id: int) -> Alocacao:
        return self.db_session.query(Alocacao).filter_by(id_alocacao=alocacao_id).first()

    def update(self, alocacao_id: int, alocacao_data: AlocacaoUpdate) -> Alocacao:
        alocacao = self.get_by_id(alocacao_id)
        if alocacao:
            for key, value in alocacao_data.dict(exclude_unset=True).items():
                setattr(alocacao, key, value)
            self.db_session.commit()
            self.db_session.refresh(alocacao)
        return alocacao

    def delete(self, alocacao_id: int):
        alocacao = self.get_by_id(alocacao_id)
        if alocacao:
            self.db_session.delete(alocacao)
            self.db_session.commit()
        return alocacao

    def list_all(self):
        return self.db_session.query(Alocacao).all()
