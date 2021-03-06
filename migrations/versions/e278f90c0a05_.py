"""empty message

Revision ID: e278f90c0a05
Revises: 
Create Date: 2022-03-26 22:14:27.523688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e278f90c0a05'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('polls',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('range_age', sa.String(length=10), nullable=False),
    sa.Column('gender', sa.String(length=1), nullable=False),
    sa.Column('favsn', sa.String(length=20), nullable=False),
    sa.Column('tfb', sa.Integer(), nullable=False),
    sa.Column('ttw', sa.Integer(), nullable=False),
    sa.Column('tins', sa.Integer(), nullable=False),
    sa.Column('twa', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('polls')
    # ### end Alembic commands ###
