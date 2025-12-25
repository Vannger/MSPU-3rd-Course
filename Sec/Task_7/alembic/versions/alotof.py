"""create_tables_and_seed_bcrypt

Revision ID: fixed_revision_bcrypt
Revises: 
Create Date: 2023-10-27 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime
from passlib.context import CryptContext

revision = 'fixed_revision_bcrypt'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('password_hash', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=True)

    op.create_table('tokens',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('value', sa.String(), nullable=True),
        sa.Column('is_valid', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tokens_value'), 'tokens', ['value'], unique=True)

    op.create_table('orders',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('goods',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('order_id', sa.Integer(), nullable=True),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('count', sa.Integer(), nullable=True),
        sa.Column('price', sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret_hash = pwd_context.hash("sysoevsecretic")

    users_table = sa.table('users',
        sa.Column('id', sa.Integer),
        sa.Column('name', sa.String),
        sa.Column('password_hash', sa.String)
    )
    
    op.bulk_insert(users_table, [
        {'id': 1, 'name': 'alice', 'password_hash': secret_hash},
        {'id': 2, 'name': 'bob', 'password_hash': secret_hash},
        {'id': 3, 'name': 'mallory', 'password_hash': secret_hash},
    ])

    tokens_table = sa.table('tokens',
        sa.Column('user_id', sa.Integer),
        sa.Column('value', sa.String),
        sa.Column('is_valid', sa.Boolean)
    )
    op.bulk_insert(tokens_table, [
        {'user_id': 1, 'value': 'secrettokenAlice', 'is_valid': True}
    ])

    orders_table = sa.table('orders',
        sa.Column('id', sa.Integer),
        sa.Column('user_id', sa.Integer),
        sa.Column('created_at', sa.DateTime)
    )
    op.bulk_insert(orders_table, [
        {'id': 1, 'user_id': 1, 'created_at': datetime.utcnow()},
        {'id': 2, 'user_id': 1, 'created_at': datetime.utcnow()}
    ])
    
    goods_table = sa.table('goods',
        sa.Column('id', sa.Integer),
        sa.Column('order_id', sa.Integer),
        sa.Column('name', sa.String),
        sa.Column('count', sa.Integer),
        sa.Column('price', sa.Float)
    )
    op.bulk_insert(goods_table, [
        {'id': 1, 'order_id': 1, 'name': 'Laptop', 'count': 1, 'price': 1000.0},
        {'id': 2, 'order_id': 1, 'name': 'Mouse', 'count': 2, 'price': 50.0},
        {'id': 3, 'order_id': 2, 'name': 'Monitor', 'count': 1, 'price': 300.0},
    ])

def downgrade() -> None:
    op.drop_table('goods')
    op.drop_table('orders')
    op.drop_index(op.f('ix_tokens_value'), table_name='tokens')
    op.drop_table('tokens')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_table('users')