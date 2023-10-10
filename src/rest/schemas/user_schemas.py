from datetime import datetime
import re

from pydantic import BaseModel, EmailStr, validator
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# from heshing import Hasher


class UserListSchemas(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: str
    phone: str
    email: EmailStr
    password: str
    created_at: datetime
    updated_at: datetime


class UserCreateSchema(BaseModel):
    first_name: str
    last_name: str
    age: str
    phone: str
    email: EmailStr
    hashed_password: str

    @validator('password')
    def validate_password(cls, value):
        pattern = r"^(?=.*[0-9])(?=.*[!@#$%^&*()_+{}|:;<>,.?~-])[A-Za-z0-9!@#$%^&*()_+{}|:;<>,.?~-]{8,}$"

        if re.match(pattern, value):
            return value
        raise ValueError('The password must consist of one special character, one number and be 8 characters long.')

    # @staticmethod
    # def get_password_hash(password: str) -> str:
    #     return pwd_context.hash(password)


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserListSchemas):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserRetrieveSchema(**user_in.dict(), hashed_password=hashed_password)
    return user_in_db


class UserRetrieveSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: str
    phone: str
    email: EmailStr
    hash_password: str
