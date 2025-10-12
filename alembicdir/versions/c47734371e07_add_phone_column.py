"""add_phone_column

Revision ID: c47734371e07
Revises: 8082de71b645
Create Date: 2025-10-11 19:53:19.834729

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c47734371e07'
down_revision: Union[str, Sequence[str], None] = '8082de71b645'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users",sa.Column("phone",sa.String(length=30),nullable=True))
    pass


def downgrade() -> None:
    op.drop_column("users","phone")
    pass
