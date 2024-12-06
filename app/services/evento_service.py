from sqlalchemy.orm import Session
from app.repositories.evento_repository import EventoRepository
from app.schemas.evento_schemas import EventoCreate, EventoUpdate


class EventoService:
    def __init__(self, db_session: Session):
        self.repository = EventoRepository(db_session)

    def create_evento(self, evento_data: EventoCreate):
        return self.repository.create(evento_data)

    def get_evento(self, id_evento: int):
        return self.repository.get_by_id(id_evento)

    def update_evento(self, id_evento: int, evento_data: EventoUpdate):
        return self.repository.update(id_evento, evento_data)

    def delete_evento(self, id_evento: int):
        return self.repository.delete(id_evento)

    def list_eventos(self):
        return self.repository.list_all()
