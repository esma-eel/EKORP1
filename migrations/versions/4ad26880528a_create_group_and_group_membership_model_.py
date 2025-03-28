"""create group and group membership model connected to user profiles

Revision ID: 4ad26880528a
Revises: 70e1219183af
Create Date: 2025-03-24 17:41:09.313899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ad26880528a'
down_revision = '70e1219183af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    with op.batch_alter_table('user_groups', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_groups_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_groups_updated_at'), ['updated_at'], unique=False)

    op.create_table('group_memberships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['user_groups.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['user_profiles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('group_memberships', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_group_memberships_created_at'), ['created_at'], unique=False)
        batch_op.create_index(batch_op.f('ix_group_memberships_updated_at'), ['updated_at'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('group_memberships', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_group_memberships_updated_at'))
        batch_op.drop_index(batch_op.f('ix_group_memberships_created_at'))

    op.drop_table('group_memberships')
    with op.batch_alter_table('user_groups', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_groups_updated_at'))
        batch_op.drop_index(batch_op.f('ix_user_groups_created_at'))

    op.drop_table('user_groups')
    # ### end Alembic commands ###
