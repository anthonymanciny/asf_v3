from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.espacoinstituicao_service import EspacoInstituicaoService
from app.schemas.espacaoinstituicao_schemas import EspacoInstituicaoCreate, EspacoInstituicaoUpdate, EspacoInstituicaoResponse
from app.db.depends import get_db

espaco_instituicao_router = APIRouter(prefix="/espacos", tags=["Espaços Institucionais"])

@espaco_instituicao_router.post("/", response_model=EspacoInstituicaoResponse)
def create_espaco(espaco_data: EspacoInstituicaoCreate, db: Session = Depends(get_db)):
    service = EspacoInstituicaoService(db)
    return service.create_espaco_instituicao(espaco_data)

@espaco_instituicao_router.get("/{espaco_id}", response_model=EspacoInstituicaoResponse)
def get_espaco(espaco_id: int, db: Session = Depends(get_db)):
    service = EspacoInstituicaoService(db)
    espaco = service.get_espaco_instituicao(espaco_id)
    if not espaco:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Espaço Institucional não encontrado")
    return espaco

@espaco_instituicao_router.put("/{espaco_id}", response_model=EspacoInstituicaoResponse)
def update_espaco(espaco_id: int, espaco_data: EspacoInstituicaoUpdate, db: Session = Depends(get_db)):
    service = EspacoInstituicaoService(db)
    espaco = service.update_espaco_instituicao(espaco_id, espaco_data)
    if not espaco:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Espaço Institucional não encontrado")
    return espaco

@espaco_instituicao_router.delete("/{espaco_id}", response_model=dict)
def delete_espaco(espaco_id: int, db: Session = Depends(get_db)):
    service = EspacoInstituicaoService(db)
    espaco = service.delete_espaco_instituicao(espaco_id)
    if not espaco:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Espaço Institucional não encontrado")
    return {"message": "Espaço Institucional deletado com sucesso"}

@espaco_instituicao_router.get("/", response_model=list[EspacoInstituicaoResponse])
def list_espacos(db: Session = Depends(get_db)):
    service = EspacoInstituicaoService(db)
    return service.list_espacos_instituicoes()
