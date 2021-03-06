"""Add X.509 relations

Revision ID: dd62dc6b60dd
Revises: 2147817b0cbe
Create Date: 2018-07-18 21:37:31.533422

"""
from alembic import op
import sqlalchemy as sa
import sq.ext.rdbms.types


# revision identifiers, used by Alembic.
revision = 'dd62dc6b60dd'
down_revision = '2147817b0cbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('certificatefingerprints',
    sa.Column('gsid', sq.ext.rdbms.types.UUID(), nullable=False),
    sa.Column('fingerprint', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('fingerprint')
    )
    op.create_table('certificatenames',
    sa.Column('gsid', sq.ext.rdbms.types.UUID(), nullable=False),
    sa.Column('issuer', sa.String(), nullable=False),
    sa.Column('subject', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('issuer', 'subject')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('certificatenames')
    op.drop_table('certificatefingerprints')
    # ### end Alembic commands ###
