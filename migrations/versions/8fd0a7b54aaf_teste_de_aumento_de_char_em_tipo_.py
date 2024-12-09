"""teste de aumento de char em tipo_participacao

Revision ID: 8fd0a7b54aaf
Revises: 1d3577367ccb
Create Date: 2024-12-09 11:32:22.620808

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8fd0a7b54aaf'
down_revision: Union[str, None] = '1d3577367ccb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('participacao', 'tipo_participacao',
               existing_type=sa.CHAR(length=1),
               type_=sa.CHAR(length=35),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('participacao', 'tipo_participacao',
               existing_type=sa.CHAR(length=35),
               type_=sa.CHAR(length=1),
               existing_nullable=False)
    # ### end Alembic commands ###