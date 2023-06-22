from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('company',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('visibility', sa.Boolean(), nullable=False),
        sa.Column('grade', sa.Numeric()),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('company')