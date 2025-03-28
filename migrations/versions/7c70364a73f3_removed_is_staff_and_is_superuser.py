"""removed is_staff and is_superuser

Revision ID: 7c70364a73f3
Revises: 03e9d705aeb4
Create Date: 2025-03-20 13:37:32.271865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c70364a73f3'
down_revision = '03e9d705aeb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('is_superuser')
        batch_op.drop_column('is_staff')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_staff', sa.BOOLEAN(), nullable=False))
        batch_op.add_column(sa.Column('is_superuser', sa.BOOLEAN(), nullable=False))

    # ### end Alembic commands ###
