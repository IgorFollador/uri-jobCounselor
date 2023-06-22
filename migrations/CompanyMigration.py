from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('company',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('visibility', sa.Boolean(), nullable=False),
        sa.Column('grade', sa.Double(), nullable=False),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('password', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('company')