"""empty message

Revision ID: 7a2d33de5001
Revises: f7e747cad379
Create Date: 2020-03-29 15:20:08.292291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a2d33de5001'
down_revision = 'f7e747cad379'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('biography', sa.String(length=80), nullable=True))
    op.add_column('user_profiles', sa.Column('date_created', sa.Date(), nullable=True))
    op.add_column('user_profiles', sa.Column('email', sa.String(length=80), nullable=True))
    op.add_column('user_profiles', sa.Column('gender', sa.String(length=10), nullable=True))
    op.add_column('user_profiles', sa.Column('location', sa.String(length=80), nullable=True))
    op.add_column('user_profiles', sa.Column('profile_pic', sa.String(length=80), nullable=True))
    op.drop_constraint('user_profiles_username_key', 'user_profiles', type_='unique')
    op.drop_column('user_profiles', 'username')
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('user_profiles', sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=True))
    op.create_unique_constraint('user_profiles_username_key', 'user_profiles', ['username'])
    op.drop_column('user_profiles', 'profile_pic')
    op.drop_column('user_profiles', 'location')
    op.drop_column('user_profiles', 'gender')
    op.drop_column('user_profiles', 'email')
    op.drop_column('user_profiles', 'date_created')
    op.drop_column('user_profiles', 'biography')
    # ### end Alembic commands ###
