"""add blacklist table

Revision ID: 05904ee12c32
Revises: 55523e93cbe3
Create Date: 2020-09-12 09:31:23.844960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05904ee12c32'
down_revision = '55523e93cbe3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_token',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blacklist_token')
    # ### end Alembic commands ###
