# from fastapi import APIRouter
#
# from src.core.db import session
# from src.core.managers.user_manager import UserManager
# from src.rest.schemas.user_schemas import UserCreateSchema
#
#
# class UserService:
#
#     @staticmethod
#     def create_user(user: UserCreateSchema):
#          return UserManager.create(input_data=user.__dict__, session=session)
