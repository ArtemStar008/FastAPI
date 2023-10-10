from fastapi import APIRouter, status

from src.core.db import session
from src.core.managers.user_manager import UserManager
from src.rest.schemas.user_schemas import UserCreateSchema, UserListSchemas, UserRetrieveSchema, fake_save_user

router = APIRouter()


@router.get('/user/list', response_model=list[UserListSchemas], status_code=status.HTTP_200_OK)
def get_users():
    return UserManager.list(session=session)


@router.post('/users')
def create_user(user: UserCreateSchema):
    return UserManager.create(input_data=user.__dict__, session=session)


@router.get('/users/{user_id}', response_model=UserRetrieveSchema, status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    return UserManager.retrieve(pk=user_id, session=session)


@router.delete('user/{user_id}', status_code=status.HTTP_200_OK)
def delete_order(user_id: int):
    return UserManager.delete(pk=user_id, session=session)


# ___________________

@router.post("/user/", response_model=UserListSchemas)
async def create_user(user_in: UserRetrieveSchema):
    user_saved = fake_save_user(user_in)
    return user_saved
