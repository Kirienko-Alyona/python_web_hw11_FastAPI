"""Init

Revision ID: 9d68fdc2be95
Revises: 
Create Date: 2023-03-30 01:05:41.682728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d68fdc2be95'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('born_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.create_index(op.f('ix_contact_email'), 'contact', ['email'], unique=True)
    op.create_index(op.f('ix_contact_id'), 'contact', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contact_id'), table_name='contact')
    op.drop_index(op.f('ix_contact_email'), table_name='contact')
    op.drop_table('contact')
    # ### end Alembic commands ###