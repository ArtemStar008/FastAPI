from fastapi import APIRouter, status

from src.core.db import session
from src.core.managers.book_manager import BookManager
from src.rest.schemas.book_schemas import BookCreateSchema, BookListSchemas, BookRetrieveSchema

router = APIRouter()


@router.get('/book/list', response_model=list[BookListSchemas], status_code=status.HTTP_200_OK)
def get_book():
    return BookManager.list(session=session)


@router.post('/books')
def create_book(book: BookCreateSchema):
    return BookManager.create(input_data=book.__dict__, session=session)


# response_model=UserRetrieveSchema, status_code=status.HTTP_200_OK
@router.get('/book/{book_name}')  # почему-то когда добавляю response model падает ошибка 500 Internal Server Error
def get_book(book_name: str):     # с юзером так не происходит
    return BookManager.retrieve_str(book_str=book_name, session=session)
