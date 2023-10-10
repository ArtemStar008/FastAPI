from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Any

from src.core.mixins.base_mixin import BaseMixin


class ListMixin(BaseMixin):

    @classmethod
    def list(cls, session: Session):
        query = select(cls.table)
        objects = session.execute(query)
        return objects.scalars().all()
