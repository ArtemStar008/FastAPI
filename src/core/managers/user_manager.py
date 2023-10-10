from src.core.managers.base_manager import BaseManager
from src.models.user_model import User


class UserManager(BaseManager):
    table = User
