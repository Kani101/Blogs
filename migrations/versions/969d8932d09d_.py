"""empty message

Revision ID: 969d8932d09d
Revises: d298d98dc64d
Create Date: 2020-07-02 08:28:22.064701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '969d8932d09d'
down_revision = 'd298d98dc64d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'contact')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('contact', sa.VARCHAR(length=10), nullable=True))
    # ### end Alembic commands ###
