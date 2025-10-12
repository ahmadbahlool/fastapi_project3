"""removevotetable

Revision ID: c78b54519205
Revises: f3f1c0bccaa3
Create Date: 2025-10-11 22:03:23.391625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c78b54519205'
down_revision: Union[str, Sequence[str], None] = 'f3f1c0bccaa3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("votes",if_exists=True)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
