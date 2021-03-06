"""empty message

Revision ID: 4c05e8316b26
Revises: 51f3b3b5cd5d
Create Date: 2017-11-28 20:20:17.590312

"""

# revision identifiers, used by Alembic.
revision = '4c05e8316b26'
down_revision = '51f3b3b5cd5d'

from alembic import op
import sqlalchemy as sa

                               


def upgrade():
    #with app.app_context() as c:
    #   db.session.add(Model())
    #   db.session.commit()
        
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('institute',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('canonical_name', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('street', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('ringgold_id', sa.Integer(), nullable=True),
    sa.Column('ads_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('library',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('libserver', sa.String(), nullable=True),
    sa.Column('iconurl', sa.String(), nullable=True),
    sa.Column('libname', sa.String(), nullable=True),
    sa.Column('institute', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['institute'], ['institute.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint(u'queries_qid_key', 'queries', type_='unique')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(u'queries_qid_key', 'queries', ['qid'])
    op.drop_table('library')
    op.drop_table('institute')
    ### end Alembic commands ###
