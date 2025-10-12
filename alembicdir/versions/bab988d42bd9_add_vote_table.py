"""add_vote_table

Revision ID: bab988d42bd9
Revises: 95193dca78bc
Create Date: 2025-10-11 21:42:10.613131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bab988d42bd9'
down_revision: Union[str, Sequence[str], None] = '95193dca78bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("votes",
                    sa.Column("productid",sa.INTEGER,sa.ForeignKey("products.productid",ondelete="CASCADE"),primary_key=True),
                    sa.Column("userid",sa.INTEGER,sa.ForeignKey("users.userid",ondelete="CASCADE"),primary_key=True))

                    
    pass


def downgrade() -> None:
    op.drop_table("votes")
    pass
