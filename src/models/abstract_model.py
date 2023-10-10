import sqlalchemy as sa
from datetime import datetime
from sqlalchemy import DateTime
from src.core.db import Base


class AbstractModel(Base):
    __abstract__ = True

    id = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    created_at = sa.Column('created_at', DateTime, default=datetime.now)
    updated_at = sa.Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)