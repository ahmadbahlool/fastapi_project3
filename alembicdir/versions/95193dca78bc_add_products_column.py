"""add_products_column

Revision ID: 95193dca78bc
Revises: c47734371e07
Create Date: 2025-10-11 21:34:29.633444

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95193dca78bc'
down_revision: Union[str, Sequence[str], None] = 'c47734371e07'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("products",sa.Column("productdelivered",sa.Boolean,server_default='false',nullable=False))
    op.add_column("products",sa.Column("owner",sa.INTEGER,sa.ForeignKey("users.userid",ondelete="CASCADE"),nullable=False))
    
    
def downgrade() -> None:
    op.drop_column("products","productdelivered")
    op.drop_column("products","owner")
    pass
