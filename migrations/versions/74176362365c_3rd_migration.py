"""3rd migration

Revision ID: 74176362365c
Revises: 8ff5a3b17991
Create Date: 2023-08-20 01:29:31.639612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74176362365c'
down_revision = '8ff5a3b17991'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('unique_key', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
