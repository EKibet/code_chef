"""Adds complete of typ boolean

Revision ID: 20a1d958bf33
Revises: 297202682133
Create Date: 2018-09-19 14:22:58.895191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20a1d958bf33'
down_revision = '297202682133'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('complete', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('projects', 'complete')
    # ### end Alembic commands ###
