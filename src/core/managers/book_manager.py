from src.core.managers.base_manager import BaseManager
from src.models.book_model import Book


class BookManager(BaseManager):
    table = Book
