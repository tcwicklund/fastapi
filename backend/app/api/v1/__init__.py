from fastapi import APIRouter
from . import users, items, auth  # Import API endpoint modules

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(items.router, prefix="/items", tags=["Items"])
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
