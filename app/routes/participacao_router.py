from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.participacao_service import ParticipacaoService
from app.schemas.participacao_schemas import ParticipacaoCreate, ParticipacaoUpdate, ParticipacaoResponse
from app.db.depends import get_db

participacao_router = APIRouter(prefix="/participacoes", tags=["Participações"])

@participacao_router.post("/", response_model=ParticipacaoResponse)
def create_participacao(participacao_data: ParticipacaoCreate, db: Session = Depends(get_db)):
    participacao_service = ParticipacaoService(db)
    return participacao_service.create_participacao(participacao_data)


@participacao_router.get("/{participacao_id}", response_model=ParticipacaoResponse)
def get_participacao(participacao_id: int, db: Session = Depends(get_db)):
    participacao_service = ParticipacaoService(db)
    participacao = participacao_service.get_participacao(participacao_id)
    if not participacao:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Participação não encontrada")
    return participacao


@participacao_router.put("/{participacao_id}", response_model=ParticipacaoResponse)
def update_participacao(participacao_id: int, participacao_data: ParticipacaoUpdate, db: Session = Depends(get_db)):
    participacao_service = ParticipacaoService(db)
    participacao = participacao_service.update_participacao(participacao_id, participacao_data)
    if not participacao:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Participação não encontrada")
    return participacao


@participacao_router.delete("/{participacao_id}", response_model=dict)
def delete_participacao(participacao_id: int, db: Session = Depends(get_db)):
    participacao_service = ParticipacaoService(db)
    participacao = participacao_service.delete_participacao(participacao_id)
    if not participacao:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Participação não encontrada")
    return {"message": "Participação deletada com sucesso"}


@participacao_router.get("/", response_model=list[ParticipacaoResponse])
def list_participacoes(db: Session = Depends(get_db)):
    participacao_service = ParticipacaoService(db)
    return participacao_service.list_participacoes()    
