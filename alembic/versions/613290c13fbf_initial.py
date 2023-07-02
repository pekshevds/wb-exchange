"""initial

Revision ID: 613290c13fbf
Revises: 
Create Date: 2023-07-02 09:15:20.039599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '613290c13fbf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sales_items',
    sa.Column('saleID', sa.String(length=15), nullable=False),
    sa.Column('gNumber', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('saleID')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sales_items')
    # ### end Alembic commands ###
