import sqlalchemy as sa
from src.models.abstract_model import AbstractModel


class Order(AbstractModel):
    __tablename__ = 'orders'

    book = sa.Column('Book name', sa.String(20), nullable=False)
    age = sa.Column('Birthdate', sa.String(10), nullable=False)
    phone = sa.Column('Phone number', sa.String(13), nullable=False)
    email = sa.Column('Email address', sa.String(50), nullable=False)
    address = sa.Column('Address', sa.String(20), nullable=False, unique=True)
    index = sa.Column('Post code', sa.Integer, nullable=False)
    comment = sa.Column('Comment', sa.Text, nullable=False)

