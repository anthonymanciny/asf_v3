from fastapi import Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from app.auth.jwt import decode_access_token  # Função para decodificar o JWT
from app.db.depends import get_db  # Dependência para obter o banco de dados
from app.schemas.pessoa_schemas import PessoaResponse  # Modelo Pydantic para resposta
from app.models.models import Pessoa  # Modelo SQLAlchemy para consulta

def get_current_user(authorization: str = Header(...), db: Session = Depends(get_db)) -> PessoaResponse:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"Authorization": "Bearer"},
    )

    # Extraí o token do cabeçalho 'Authorization'
    token = authorization.split(" ")[1] if authorization else None  # Obtém o token após 'Bearer'

    if token is None:
        raise credentials_exception

    # Decodifica o token JWT
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception

    username: str = payload.get("sub")  # 'sub' carrega o identificador do usuário
    if username is None:
        raise credentials_exception

    # Busca o usuário no banco de dados
    user = db.query(Pessoa).filter(Pessoa.email == username).first()
    if user is None:
        raise credentials_exception

    return PessoaResponse(
        id_pessoa=user.id_pessoa,
        nome=user.nome,
        email=user.email,
        celular=user.celular,
        telefone=user.telefone,
        cpf=user.cpf,
        data_nascimento=user.data_nascimento,
        genero=user.genero
    )
