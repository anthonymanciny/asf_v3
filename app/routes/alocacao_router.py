from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.alocacao_schemas import AlocacaoCreate, AlocacaoUpdate, AlocacaoResponse
from app.services.alocacao_service import AlocacaoService
from app.db.depends import get_db

alocacao_router = APIRouter(prefix="/alocacoes", tags=["Alocacoes"])

@alocacao_router.post("/", response_model=AlocacaoResponse)
def create_alocacao(alocacao_create: AlocacaoCreate, db: Session = Depends(get_db)):
    service = AlocacaoService(db)
    return service.create_alocacao(alocacao_create)


@alocacao_router.get("/{alocacao_id}", response_model=AlocacaoResponse)
def get_alocacao(alocacao_id: int, db: Session = Depends(get_db)):
    service = AlocacaoService(db)
    alocacao = service.get_alocacao(alocacao_id)
    if alocacao is None:
        raise HTTPException(status_code=404, detail="Alocacao not found")
    return alocacao


@alocacao_router.put("/{alocacao_id}", response_model=AlocacaoResponse)
def update_alocacao(alocacao_id: int, alocacao_update: AlocacaoUpdate, db: Session = Depends(get_db)):
    service = AlocacaoService(db)
    alocacao = service.update_alocacao(alocacao_id, alocacao_update)
    if alocacao is None:
        raise HTTPException(status_code=404, detail="Alocacao not found")
    return alocacao


@alocacao_router.delete("/{alocacao_id}", response_model=AlocacaoResponse)
def delete_alocacao(alocacao_id: int, db: Session = Depends(get_db)):
    service = AlocacaoService(db)
    alocacao = service.delete_alocacao(alocacao_id)
    if alocacao is None:
        raise HTTPException(status_code=404, detail="Alocacao not found")
    return alocacao

@alocacao_router.get("/", response_model=list[AlocacaoResponse])
def list_alocacoes(db: Session = Depends(get_db)):
    service = AlocacaoService(db)
    return service.list_alocacoes()