from fastapi import APIRouter, Depends, HTTPException
from app.services.user_service import get_current_user
from app.db.session import Session
from app.db.models import User
from sqlalchemy.orm import Session as SQLSession
from app.core.security import verify_token

router = APIRouter()


# User info endpoint (secured)
@router.get("/me", response_model=User)
async def get_me(current_user: User = Depends(get_current_user)):
    """Get current logged-in user info"""
    return current_user
