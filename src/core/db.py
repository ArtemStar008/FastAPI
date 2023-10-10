# файл отвечающий за подключение к БД

from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///test.db', echo=True, connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)  # metaclass
session = Session()

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    id = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    created_at = sa.Column('Created time', sa.DateTime(), default=datetime.now)
    update_at = sa.Column('Update time', sa.DateTime(), default=datetime.now, onupdate=datetime.now)
