"""add playlists.tracks_last_refreshed_at

Revision ID: 743b32dde3e8
Revises: 
Create Date: 2022-08-30 22:12:10.337434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '743b32dde3e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('playlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spotify_id', sa.String(length=22), nullable=False),
    sa.Column('tracks_last_refreshed_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_playlists_spotify_id'), 'playlists', ['spotify_id'], unique=True)
    op.create_table('tracks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('spotify_id', sa.String(length=22), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tracks_name'), 'tracks', ['name'], unique=False)
    op.create_index(op.f('ix_tracks_spotify_id'), 'tracks', ['spotify_id'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('playlist_track',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('playlist_id', sa.Integer(), nullable=True),
    sa.Column('track_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlists.id'], ),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('playlist_track')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_tracks_spotify_id'), table_name='tracks')
    op.drop_index(op.f('ix_tracks_name'), table_name='tracks')
    op.drop_table('tracks')
    op.drop_index(op.f('ix_playlists_spotify_id'), table_name='playlists')
    op.drop_table('playlists')
    # ### end Alembic commands ###