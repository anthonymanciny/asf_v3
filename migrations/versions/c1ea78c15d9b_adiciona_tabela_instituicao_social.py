"""Adiciona tabela instituicao_social

Revision ID: c1ea78c15d9b
Revises: 720a7fd59182
Create Date: 2024-12-06 13:17:13.829251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1ea78c15d9b'
down_revision: Union[str, None] = '720a7fd59182'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eventos',
    sa.Column('id_evento', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome_evento', sa.String(length=35), nullable=False),
    sa.Column('responsavel_evento', sa.String(length=35), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_evento')
    )
    op.create_table('instituicao_social',
    sa.Column('id_instituicao', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=35), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('endereco', sa.String(length=60), nullable=False),
    sa.Column('telefone', sa.CHAR(length=11), nullable=False),
    sa.Column('observacao', sa.String(length=100), nullable=True),
    sa.CheckConstraint('length(telefone) = 11', name='check_telefone_length'),
    sa.PrimaryKeyConstraint('id_instituicao')
    )
    op.create_table('espaco_instituicao',
    sa.Column('id_espaco_instituicao', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_instituicao', sa.Integer(), nullable=True),
    sa.Column('nome_espaco', sa.String(length=30), nullable=False),
    sa.Column('capacidade', sa.Integer(), nullable=False),
    sa.Column('responsavel', sa.String(length=35), nullable=False),
    sa.ForeignKeyConstraint(['id_instituicao'], ['instituicao_social.id_instituicao'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_espaco_instituicao')
    )
    op.create_table('participacao',
    sa.Column('id_participacao', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_evento', sa.Integer(), nullable=True),
    sa.Column('id_pessoa', sa.Integer(), nullable=True),
    sa.Column('tipo_participacao', sa.CHAR(length=1), nullable=False),
    sa.ForeignKeyConstraint(['id_evento'], ['eventos.id_evento'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_pessoa'], ['pessoas.id_pessoa'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_participacao')
    )
    op.create_table('alocacao',
    sa.Column('id_alocacao', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_evento', sa.Integer(), nullable=True),
    sa.Column('id_instituicao', sa.Integer(), nullable=True),
    sa.Column('id_espaco_instituicao', sa.Integer(), nullable=True),
    sa.Column('datahora', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('responsavel_local', sa.String(length=35), nullable=False),
    sa.ForeignKeyConstraint(['id_espaco_instituicao'], ['espaco_instituicao.id_espaco_instituicao'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_evento'], ['eventos.id_evento'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_instituicao'], ['instituicao_social.id_instituicao'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_alocacao')
    )
    op.create_index('idx_cpf_pessoa', 'pessoas', ['cpf'], unique=False)
    op.create_index('idx_email_pessoa', 'pessoas', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_email_pessoa', table_name='pessoas')
    op.drop_index('idx_cpf_pessoa', table_name='pessoas')
    op.drop_table('alocacao')
    op.drop_table('participacao')
    op.drop_table('espaco_instituicao')
    op.drop_table('instituicao_social')
    op.drop_table('eventos')
    # ### end Alembic commands ###