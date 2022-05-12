"""Initial Migration

Revision ID: e806e2e734d6
Revises: dc793f954d9d
Create Date: 2022-05-12 14:06:30.607117

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e806e2e734d6'
down_revision = 'dc793f954d9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.add_column('pitches', sa.Column('description', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('title', sa.String(), nullable=True))
    op.alter_column('pitches', 'category',
               existing_type=sa.VARCHAR(length=1000),
               nullable=False)
    op.create_index(op.f('ix_pitches_description'), 'pitches', ['description'], unique=False)
    op.drop_constraint('pitches_users_id_fkey', 'pitches', type_='foreignkey')
    op.create_foreign_key(None, 'pitches', 'users', ['owner_id'], ['id'])
    op.drop_column('pitches', 'data')
    op.drop_column('pitches', 'date')
    op.drop_column('pitches', 'users_id')
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=225), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.add_column('pitches', sa.Column('users_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('data', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.create_foreign_key('pitches_users_id_fkey', 'pitches', 'users', ['users_id'], ['id'])
    op.drop_index(op.f('ix_pitches_description'), table_name='pitches')
    op.alter_column('pitches', 'category',
               existing_type=sa.VARCHAR(length=1000),
               nullable=True)
    op.drop_column('pitches', 'title')
    op.drop_column('pitches', 'description')
    op.drop_column('pitches', 'owner_id')
    # ### end Alembic commands ###