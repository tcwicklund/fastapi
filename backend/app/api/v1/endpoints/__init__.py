# This file is used to create the API router for the application
from fastapi import APIRouter

from . import users, items, auth

# Import the routers from the API endpoints
router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(items.router, prefix="/items", tags=["Items"])
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
