from sqlalchemy import (
    Column,
    String,
    Integer,
    Date,
    DateTime,
    ForeignKey,
    CHAR,
    CheckConstraint,
    Index
)
from sqlalchemy.orm import relationship
from app.db.base import Base

# Tabela Instituicao
class Instituicao(Base):
    __tablename__ = 'instituicao_social'

    id_instituicao = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(35), nullable=False)
    email = Column(String(50), nullable=False)
    endereco = Column(String(60), nullable=False)
    telefone = Column(CHAR(11), nullable=False)
    observacao = Column(String(100), nullable=True)

    __table_args__ = (
        CheckConstraint("length(telefone) = 11", name="check_telefone_length"),
    )

    alocacoes = relationship('Alocacao', back_populates='instituicao')
    espacos = relationship('EspacoInstituicao', back_populates='instituicao')

# Tabela EspacoInstituicao
class EspacoInstituicao(Base):
    __tablename__ = 'espaco_instituicao'

    id_espaco_instituicao = Column(Integer, primary_key=True, autoincrement=True)
    id_instituicao = Column(Integer, ForeignKey('instituicao_social.id_instituicao', ondelete='CASCADE'))
    nome_espaco = Column(String(30), nullable=False)
    capacidade = Column(Integer, nullable=False)
    responsavel = Column(String(35), nullable=False)

    instituicao = relationship('Instituicao', back_populates='espacos')
    alocacoes = relationship('Alocacao', back_populates='espaco')

# Tabela Pessoa
class Pessoa(Base):
    __tablename__ = 'pessoas'

    id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(35), nullable=False)
    senha = Column(String(60), nullable=False)  # Deve ser hash e salt
    email = Column(String(50), unique=True, nullable=False, index=True)
    celular = Column(CHAR(11), CheckConstraint("length(celular) = 11"), unique=True, nullable=False)
    telefone = Column(CHAR(11), unique=True, nullable=True)
    cpf = Column(CHAR(11), CheckConstraint("length(cpf) = 11"), unique=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    genero = Column(CHAR(1), nullable=True)

    participacoes = relationship('Participacao', back_populates='pessoa')

# Tabela Alocacao
class Alocacao(Base):
    __tablename__ = 'alocacao'

    id_alocacao = Column(Integer, primary_key=True, autoincrement=True)
    id_evento = Column(Integer, ForeignKey('eventos.id_evento', ondelete='CASCADE'))
    id_instituicao = Column(Integer, ForeignKey('instituicao_social.id_instituicao', ondelete='CASCADE'))
    id_espaco_instituicao = Column(Integer, ForeignKey('espaco_instituicao.id_espaco_instituicao', ondelete='CASCADE'))
    datahora = Column(DateTime, nullable=False)
    status = Column(Integer, nullable=False)
    responsavel_local = Column(String(35), nullable=False)

    evento = relationship('Evento', back_populates='alocacoes')
    instituicao = relationship('Instituicao', back_populates='alocacoes')
    espaco = relationship('EspacoInstituicao', back_populates='alocacoes')

# Tabela Evento
class Evento(Base):
    __tablename__ = 'eventos'

    id_evento = Column(Integer, primary_key=True, autoincrement=True)
    nome_evento = Column(String(35), nullable=False)
    responsavel_evento = Column(String(35), nullable=False)
    status = Column(Integer, nullable=False)  # Agora trabalha com Status com valores 1 ou 0

    alocacoes = relationship('Alocacao', back_populates='evento')
    participacoes = relationship('Participacao', back_populates='evento')

# Tabela Participacao
class Participacao(Base):
    __tablename__ = 'participacao'

    id_participacao = Column(Integer, primary_key=True, autoincrement=True)
    id_evento = Column(Integer, ForeignKey('eventos.id_evento', ondelete='CASCADE'))
    id_pessoa = Column(Integer, ForeignKey('pessoas.id_pessoa', ondelete='CASCADE'))
    tipo_participacao = Column(CHAR(35), nullable=False)

    evento = relationship('Evento', back_populates='participacoes')
    pessoa = relationship('Pessoa', back_populates='participacoes')

# Índices adicionais para desempenho
Index('idx_email_pessoa', Pessoa.email)
Index('idx_cpf_pessoa', Pessoa.cpf)
