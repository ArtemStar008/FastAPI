import sqlalchemy as sa
from src.models.abstract_model import AbstractModel


class User(AbstractModel):
    __tablename__ = 'users'

    first_name = sa.Column('First name', sa.String(20), nullable=False)
    last_name = sa.Column('Last name', sa.String(20), nullable=False)
    age = sa.Column('Birthdate', sa.String(10), nullable=False)
    phone = sa.Column('Phone number', sa.String(13), nullable=False, unique=True)
    email = sa.Column('Email address', sa.String(50), nullable=False, unique=True)
    password = sa.Column('Password', sa.Text, nullable=False)
