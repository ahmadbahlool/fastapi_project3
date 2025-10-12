"""add_columns

Revision ID: 09712ca4c27d
Revises: 1c921190673e
Create Date: 2025-10-11 19:34:19.376921

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column,INTEGER,TIMESTAMP
from typing import Text
from sqlalchemy.sql.expression import text

# revision identifiers, used by Alembic.
revision: str = '09712ca4c27d'
down_revision: Union[str, Sequence[str], None] = '1c921190673e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("products",Column("createdat",TIMESTAMP(timezone=True),nullable=False,server_default=text('now()')))
    pass


def downgrade() -> None:
    op.drop_column("products","createdat")
    pass
