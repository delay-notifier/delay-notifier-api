from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.schemas.user import User
from app.database import get_db
from app.crud import user as user_crud
from typing import Optional
from datetime import datetime, timedelta, timezone
import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY", "DUMMY_SECRET_KEY_FOR_DEVELOPMENT_ONLY")
ALGORITHM = "HS256"

denylist: set[str] = set()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")

def create_access_token(data: dict, expires_delta: Optional[datetime] = None) -> str:
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

def is_token_revoked(token: str) -> bool:
    return token in denylist

async def revoke_token(token: str) -> None:
    denylist.add(token)

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    if is_token_revoked(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has been revoked",
            headers={"WWW-Authenticate": "Bearer"},
        )
    payload = decode_token(token)
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = user_crud.get_user(db, user_id=int(user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user