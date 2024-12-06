# app/routes/instituicao_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.instituicao_schemas import InstituicaoCreate, InstituicaoUpdate, InstituicaoResponse
from app.services.instituicao_service import InstituicaoService
from app.db.depends import get_db

instituticao_router = APIRouter(prefix="/instituicoes", tags=["Instituicoes"])


@instituticao_router.post("/", response_model=InstituicaoResponse)
def create_instituicao(instituicao_create: InstituicaoCreate, db: Session = Depends(get_db)):
    service = InstituicaoService(db)
    return service.create_instituicao(instituicao_create)


@instituticao_router.get("/{instituicao_id}", response_model=InstituicaoResponse)
def get_instituicao(instituicao_id: int, db: Session = Depends(get_db)):
    service = InstituicaoService(db)
    instituicao = service.get_instituicao(instituicao_id)
    if instituicao is None:
        raise HTTPException(status_code=404, detail="Instituicao not found")
    return instituicao


@instituticao_router.get("/", response_model=list[InstituicaoResponse])
def list_instituicoes(get_db: Session = Depends(get_db)):
    pessoa = InstituicaoService(get_db)
    return pessoa.list_instituicoes()


@instituticao_router.put("/{instituicao_id}", response_model=InstituicaoResponse)
def update_instituicao(instituicao_id: int, instituicao_update: InstituicaoUpdate, db: Session = Depends(get_db)):
    service = InstituicaoService(db)
    instituicao = service.update_instituicao(instituicao_id, instituicao_update)
    if instituicao is None:
        raise HTTPException(status_code=404, detail="Instituicao not found")
    return instituicao


@instituticao_router.delete("/{instituicao_id}", response_model=InstituicaoResponse)
def delete_instituicao(instituicao_id: int, db: Session = Depends(get_db)):
    service = InstituicaoService(db)
    instituicao = service.delete_instituicao(instituicao_id)
    if instituicao is None:
        raise HTTPException(status_code=404, detail="Instituicao not found")
    return instituicao
