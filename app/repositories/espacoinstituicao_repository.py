from sqlalchemy.orm import Session
from app.models.models import EspacoInstituicao
from app.schemas.espacaoinstituicao_schemas import EspacoInstituicaoCreate, EspacoInstituicaoUpdate


class EspacoInstituicaoRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, espaco_instituicao_data: EspacoInstituicaoCreate) -> EspacoInstituicao:
        espaco_instituicao = EspacoInstituicao(**espaco_instituicao_data.dict())
        self.db_session.add(espaco_instituicao)
        self.db_session.commit()
        self.db_session.refresh(espaco_instituicao)
        return espaco_instituicao

    def get_by_id(self, espaco_instituicao_id: int) -> EspacoInstituicao:
        return self.db_session.query(EspacoInstituicao).filter_by(espaco_instituicao_id=espaco_instituicao_id).first()

    def update(self, espaco_instituicao_id: int, espaco_instituicao_data: EspacoInstituicaoUpdate) -> EspacoInstituicao:
        espaco_instituicao = self.get_by_id(espaco_instituicao_id)
        if espaco_instituicao:
            for key, value in espaco_instituicao_data.dict(exclude_unset=True).items():
                setattr(espaco_instituicao, key, value)
            self.db_session.commit()
            self.db_session.refresh(espaco_instituicao)
        return espaco_instituicao

    def delete(self, espaco_instituicao_id: int):
        espaco_instituicao = self.get_by_id(espaco_instituicao_id)
        if espaco_instituicao:
            self.db_session.delete(espaco_instituicao)
            self.db_session.commit()
        return espaco_instituicao

    def list_all(self):
        return self.db_session.query(EspacoInstituicao).all()
