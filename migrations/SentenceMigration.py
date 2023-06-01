from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('senteces',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('sentence', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('users')