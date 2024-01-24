"""rank roles added

Revision ID: f317c66a39d5
Revises: 4cc5a9a2f71e
Create Date: 2024-01-24 15:03:26.373295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f317c66a39d5'
down_revision: Union[str, None] = '4cc5a9a2f71e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_manager', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_deleted')
    op.drop_column('users', 'is_manager')
    # ### end Alembic commands ###