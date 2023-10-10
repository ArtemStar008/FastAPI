from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BookListSchemas(BaseModel):
    book: str
    author: str
    genre: str
    price: float
    description: str
    hardcover: bool
    weight: int


class BookCreateSchema(BaseModel):
    book: str
    author: str
    genre: str
    price: float
    description: str
    hardcover: bool
    weight: int


class BookRetrieveSchema(BaseModel):
    book: str
    author: str
    genre: str
    price: float
    description: str
    hardcover: bool
    weight: int
