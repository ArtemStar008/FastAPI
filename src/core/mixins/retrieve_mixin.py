from sqlalchemy.orm import Session
from src.core.mixins.base_mixin import BaseMixin


class RetrieveMixin(BaseMixin):
    @classmethod
    def retrieve(cls, pk: int, session: Session):
        return session.query(cls.table).get(pk)

    @classmethod
    def retrieve_str(cls, book_str: str, session: Session):
        return session.query(cls.table).filter(cls.table.book == book_str).first()
