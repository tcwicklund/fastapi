from fastapi import APIRouter, HTTPException, Depends
from app.schemas import UserCreate, UserRead, UserLogin
from app.services.user_service import authenticate_user, create_user
from app.db.session import Session
from app.db.models import User
from sqlalchemy.orm import Session as SQLSession
from app.core.security import create_access_token

router = APIRouter()


# User Registration
@router.post("/register", response_model=UserRead)
async def register_user(user_create: UserCreate, db: SQLSession = Depends(get_db)):
    """Register a new user"""
    existing_user = db.query(User).filter(User.email == user_create.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = create_user(user_create, db)
    return user


# User Login
@router.post("/login", response_model=str)
async def login_user(user_login: UserLogin, db: SQLSession = Depends(get_db)):
    """Login an existing user"""
    user = authenticate_user(user_login, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Generate and return JWT token
    access_token = create_access_token(data={"sub": user.email})
    return access_token
