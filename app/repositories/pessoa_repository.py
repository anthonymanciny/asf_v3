from sqlalchemy.orm import Session
from app.models.models import Pessoa
from app.schemas.pessoa_schemas import PessoaCreate, PessoaUpdate
from passlib.context import CryptContext

# Contexto do PassLib para hashing de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class PessoaRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create(self, pessoa_data: PessoaCreate) -> Pessoa:
        # Hash da senha antes de armazenar no banco de dados
        hashed_password = self.hash_password(pessoa_data.senha)
        
        pessoa = Pessoa(
            nome=pessoa_data.nome,
            senha=hashed_password,  # Armazenando a senha hash
            email=pessoa_data.email,
            celular=pessoa_data.celular,
            telefone=pessoa_data.telefone,
            cpf=pessoa_data.cpf,
            data_nascimento=pessoa_data.data_nascimento,
            genero=pessoa_data.genero
        )
        
        self.db_session.add(pessoa)
        self.db_session.commit()
        self.db_session.refresh(pessoa)
        return pessoa

    def get_by_id(self, pessoa_id: int) -> Pessoa:
        return self.db_session.query(Pessoa).filter_by(id_pessoa=pessoa_id).first()

    def update(self, pessoa_id: int, pessoa_data: PessoaUpdate) -> Pessoa:
        pessoa = self.get_by_id(pessoa_id)
        if pessoa:
            for key, value in pessoa_data.dict(exclude_unset=True).items():
                setattr(pessoa, key, value)
            self.db_session.commit()
            self.db_session.refresh(pessoa)
        return pessoa

    def delete(self, pessoa_id: int):
        pessoa = self.get_by_id(pessoa_id)
        if pessoa:
            self.db_session.delete(pessoa)
            self.db_session.commit()
        return pessoa

    def list_all(self):
        return self.db_session.query(Pessoa).all()
    

    # Método para fazer o hash da senha
    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)
