from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.services.pessoa_service import PessoaService
from app.schemas.pessoa_schemas import PessoaCreate, PessoaUpdate, PessoaResponse
from app.db.depends import get_db

pessoa_router = APIRouter(prefix="/pessoas", tags=["Pessoas"])

@pessoa_router.post("/", response_model=PessoaResponse)
def create_pessoa(pessoa_data: PessoaCreate, get_db: Session = Depends(get_db)):
    pessoa = PessoaService(get_db)
    return pessoa.create_pessoa(pessoa_data)


@pessoa_router.get("/{pessoa_id}", response_model=PessoaResponse)
def get_pessoa(pessoa_id: int, get_db: Session = Depends(get_db)):
    pessoa = PessoaService(get_db)
    pessoa = pessoa.get_pessoa(pessoa_id)
    if not pessoa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa not found")
    return pessoa


@pessoa_router.put("/{pessoa_id}", response_model=PessoaResponse)
def update_pessoa(pessoa_id: int, pessoa_data: PessoaUpdate, get_db: Session = Depends(get_db)):
    pessoa = PessoaService(get_db)
    pessoa = pessoa.update_pessoa(pessoa_id, pessoa_data)
    if not pessoa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa not found")
    return pessoa


@pessoa_router.delete("/{pessoa_id}", response_model=dict)
def delete_pessoa(pessoa_id: int, get_db: Session = Depends(get_db)):
    pessoa = PessoaService(get_db)
    pessoa = pessoa.delete_pessoa(pessoa_id)
    if not pessoa:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa not found")
    return {"message": "Pessoa deleted successfully"}


@pessoa_router.get("/", response_model=list[PessoaResponse])
def list_pessoas(get_db: Session = Depends(get_db)):
    pessoa = PessoaService(get_db)
    return pessoa.list_pessoas()
