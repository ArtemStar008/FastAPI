import sqlalchemy as sa
from src.models.abstract_model import AbstractModel


class Book(AbstractModel):
    __tablename__ = 'books'

    book = sa.Column('Book name', sa.String(30), nullable=False)
    author = sa.Column('Author name', sa.String(30), nullable=False)
    genre = sa.Column('Book genre', sa.String(30), nullable=False)
    price = sa.Column('Book price', sa.Float, nullable=False)
    description = sa.Column('Description', sa.Text, nullable=False)
    hardcover = sa.Column('Hardcover', sa.Boolean, default=False)
    weight = sa.Column('Weight in grams', sa.Integer, nullable=False)
