"""add_hit_rate_to_company_logo_table

Revision ID: 9e83fdbcd53b
Revises: 
Create Date: 2024-03-11 11:32:38.281075

"""
from typing import Sequence, Union
from sqlalchemy.dialects.mysql import BIGINT
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9e83fdbcd53b"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    try:
        print("upgrade revision=[{}]".format(revision))
        op.add_column(
            "active",
            sa.Column("hit_rate", BIGINT(), nullable=False, index=False),
        )
    except Exception as e:
        print("ERROR: upgrade=[{}]".format(str(e)))


def downgrade() -> None:
    try:
        print("downgrade revision=[{}]".format(down_revision))
        op.drop_column("active", "hit_rate")
    except Exception as e:
        print("ERROR: downgrade=[{}]".format(str(e)))
