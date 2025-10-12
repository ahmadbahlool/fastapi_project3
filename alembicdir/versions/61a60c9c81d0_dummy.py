"""dummy

Revision ID: 61a60c9c81d0
Revises: 
Create Date: 2025-10-12 22:48:29.193838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61a60c9c81d0'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("student",sa.Column("studnetid",sa.INTEGER,primary_key=True,index=True))
    pass


def downgrade() -> None:
    op.drop_table("student")
    pass
