from fastapi import APIRouter
from product.api.category import router as category_router
from product.api.product import router as product_router


router = APIRouter()
router.include_router(category_router, prefix="/category")
router.include_router(product_router, prefix="/product")
