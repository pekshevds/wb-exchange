"""init commit

Revision ID: ac86023128d9
Revises: 
Create Date: 2023-07-02 09:55:32.436842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac86023128d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sales_items',
    sa.Column('saleID', sa.String(length=15), nullable=False),
    sa.Column('gNumber', sa.String(length=50), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('lastChangeDate', sa.DateTime(), nullable=True),
    sa.Column('supplierArticle', sa.String(length=75), nullable=True),
    sa.Column('techSize', sa.String(length=30), nullable=True),
    sa.Column('barcode', sa.String(length=30), nullable=True),
    sa.Column('totalPrice', sa.Numeric(), nullable=True),
    sa.Column('discountPercent', sa.Integer(), nullable=True),
    sa.Column('isSupply', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('saleID')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sales_items')
    # ### end Alembic commands ###