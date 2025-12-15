from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.schemas.user import User
from typing import Optional

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")

async def get_user_by_email(email: str) -> Optional[User]:
    if email == "test@example.com":
        return User(
            id=1,
            email="test@example.com",
            password="password123"
        )
    return None

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    if token != "fake_token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return User(
        id=1,
        email="test@example.com",
        password="password123"
    )