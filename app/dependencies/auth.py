from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.schemas.user import User
from typing import Optional
from datetime import datetime, timedelta, timezone
import jwt
from pydantic import EmailStr

SECRET_KEY = "DUMMY_SECRET_KEY"
ALGORITHM = "HS256"

denylist: set[str] = set()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")

async def get_user_by_email(email: EmailStr) -> Optional[User]:
    if email == "test@example.com":
        return User(
            id=1,
            email="test@example.com",
            password="DUMMY_HASHED_PASSWORD"
        )
    return None

async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return plain_password == "password123"

async def get_user_by_id(user_id: int) -> Optional[User]:
    if user_id == 1:
        return User(
            id=1,
            email="test@example.com",
            password="DUMMY_HASHED_PASSWORD"
        )
    return None

def create_access_token(data: dict, expires_delta: Optional[int] = None) -> str:
    to_encode = data.copy()
    now = datetime.now(timezone.utc)

    expire = now + (expires_delta or timedelta(minutes=15))

    to_encode.update({"exp": expire, "iat": now})

    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token signature or format",
            headers={"WWW-Authenticate": "Bearer"},
        )

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    payload = decode_token(token)
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = await get_user_by_id(int(user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user