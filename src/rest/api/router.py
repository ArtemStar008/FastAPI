from fastapi import APIRouter
from src.rest.api.book import router as book_router
from src.rest.api.user import router as user_router
from src.rest.api.order import router as order_router

router = APIRouter()

router.include_router(book_router, prefix='/v1')
router.include_router(user_router, prefix='/v1')
router.include_router(order_router, prefix='/v1')