"""create tables

Revision ID: 1c921190673e
Revises: 
Create Date: 2025-10-11 18:42:38.687199

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column,INTEGER,String


# revision identifiers, used by Alembic.
revision: str = '1c921190673e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("products",Column("productid",INTEGER,index=True,primary_key=True),
                    Column("productname",String(length=20),nullable=False),
                    Column("productdescription",String(),nullable=True)
                    
                    )
    pass


def downgrade() -> None:
    op.drop_table("products")
    
    pass
