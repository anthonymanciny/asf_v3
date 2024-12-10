from sqlalchemy.orm import Session
from app.models.models import Evento
from app.schemas.evento_schemas import EventoCreate, EventoUpdate

class EventoRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, evento_data: EventoCreate) -> Evento:
        # Cria um novo evento com os dados recebidos
        evento = Evento(
            nome_evento=evento_data.nome_evento,
            responsavel_evento=evento_data.responsavel_evento,
            status=evento_data.status  # O valor já será passado corretamente
        )
        
        self.db_session.add(evento)
        self.db_session.commit()
        self.db_session.refresh(evento)
        return evento

    def get_by_id(self, evento_id: int) -> Evento:
        return self.db_session.query(Evento).filter_by(id_evento=evento_id).first()

    def update(self, evento_id: int, evento_data: EventoUpdate) -> Evento:
        evento = self.get_by_id(evento_id)
        if evento:
            for key, value in evento_data.dict(exclude_unset=True).items():
                setattr(evento, key, value)
            self.db_session.commit()
            self.db_session.refresh(evento)
        return evento

    def delete(self, evento_id: int):
        evento = self.get_by_id(evento_id)
        if evento:
            self.db_session.delete(evento)
            self.db_session.commit()
        return evento

    def list_all(self):
        return self.db_session.query(Evento).all()
