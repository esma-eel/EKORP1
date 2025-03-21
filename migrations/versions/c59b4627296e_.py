"""empty message

Revision ID: c59b4627296e
Revises: 0789ecb163ba
Create Date: 2024-12-22 16:01:30.984732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c59b4627296e'
down_revision = '0789ecb163ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('is_staff', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('is_superuser', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=False))
        batch_op.create_index(batch_op.f('ix_users_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_users_updated_at'), ['updated_at'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_updated_at'))
        batch_op.drop_index(batch_op.f('ix_users_created_at'))
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('is_superuser')
        batch_op.drop_column('is_staff')
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###
