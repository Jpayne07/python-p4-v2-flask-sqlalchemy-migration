"""update address

Revision ID: 2597f21f11aa
Revises: bf1fb4102e99
Create Date: 2024-11-22 23:47:04.137250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2597f21f11aa'
down_revision = 'bf1fb4102e99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
