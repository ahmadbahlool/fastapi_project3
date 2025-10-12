"""remove_phone

Revision ID: f3f1c0bccaa3
Revises: bab988d42bd9
Create Date: 2025-10-11 21:55:43.547265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f3f1c0bccaa3'
down_revision: Union[str, Sequence[str], None] = 'bab988d42bd9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("users","phone")
    pass


def downgrade() -> None:
    op.add_column("users",sa.Column("phone",sa.String(length=30),nullable=False))
    pass
