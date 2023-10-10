from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from src.rest.schemas.remove_nullable_value_schema import RemoveNullableValueSchema


class OrderListSchemas(BaseModel):
    id: int
    book: str
    age: Optional[int]
    phone: str
    email: EmailStr
    address: str
    index: int
    comment: str
    created_at: datetime
    updated_at: datetime


class OrderCreateSchemas(BaseModel):
    book: str
    phone: str
    email: EmailStr
    address: str
    index: int
    comment: str
    created_at: datetime
    updated_at: datetime


class OrderUpdateInputSchema(RemoveNullableValueSchema):
    book: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    index: Optional[int] = None
    comment: Optional[str] = None


class OrderUpdateResponseSchema(BaseModel):
    id: int
    book: str
    age: Optional[int]
    phone: str
    email: EmailStr
    address: str
    index: int
    comment: str
    created_at: datetime
    updated_at: datetime
