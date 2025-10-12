"""autogenerate_vote

Revision ID: 96b427b8f2c4
Revises: c78b54519205
Create Date: 2025-10-11 22:05:12.102976

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96b427b8f2c4'
down_revision: Union[str, Sequence[str], None] = 'c78b54519205'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
