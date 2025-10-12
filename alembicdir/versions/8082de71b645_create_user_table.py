"""create_user_table

Revision ID: 8082de71b645
Revises: 09712ca4c27d
Create Date: 2025-10-11 19:46:57.369162

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8082de71b645'
down_revision: Union[str, Sequence[str], None] = '09712ca4c27d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",sa.Column("userid",sa.INTEGER,index=True,primary_key=True),
                    sa.Column("username",sa.String(length=20),nullable=False,unique=True),
                    sa.Column("useremail",sa.String(length=30),unique=True,nullable=False),
                    sa.Column("createdat",sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.sql.expression.text('now()')),
                    sa.Column("userpassword",sa.String(length=30),nullable=False))

    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
