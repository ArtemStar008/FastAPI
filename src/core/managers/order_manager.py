from src.core.managers.base_manager import BaseManager
from src.models.order_model import Order


class OrderManager(BaseManager):
    table = Order
