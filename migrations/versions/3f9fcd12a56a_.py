"""empty message

Revision ID: 3f9fcd12a56a
Revises: cd82ddf60160
Create Date: 2024-05-06 04:07:02.203935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f9fcd12a56a'
down_revision = 'cd82ddf60160'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('names', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('age')
        batch_op.drop_column('last_name')
        batch_op.drop_column('names')

    # ### end Alembic commands ###
