from fastapi import APIRouter, status

from src.core.db import session
from src.core.managers.order_manager import OrderManager
from src.rest.schemas.order_schemas import OrderCreateSchemas, OrderListSchemas, OrderUpdateInputSchema

router = APIRouter()


@router.get('/order/list', response_model=list[OrderListSchemas], status_code=status.HTTP_200_OK)
def get_orders():
    return OrderManager.list(session=session)


@router.post('/order')
def create_order(order: OrderCreateSchemas):
    return OrderManager.create(input_data=order.__dict__, session=session)


@router.patch('order/{order_id}', response_model=OrderUpdateInputSchema, status_code=status.HTTP_202_ACCEPTED)
def update_user(order_id: int, input_data: OrderUpdateInputSchema):
    return OrderManager.update(pk=order_id, input_data=input_data.__dict__, session=session)


@router.delete('order/{order_id}', status_code=status.HTTP_200_OK)
def delete_order(order_id: int):
    return OrderManager.delete(pk=order_id, session=session)
