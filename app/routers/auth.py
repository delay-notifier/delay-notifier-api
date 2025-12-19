from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from app.schemas.user import UserCreate, UserResponse, User
from app.schemas.auth import LoginResponse, LogoutResponse
from app.schemas.user import User
from datetime import timedelta
from app.dependencies.auth import get_current_user, revoke_token, oauth2_scheme
from app.dependencies.auth import (
    get_current_user,
    get_user_by_email,
    verify_password,
    create_access_token,
)

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
async def signup(user_body: UserCreate):
    return UserResponse(
        id=1,
        email=user_body.email
    )

@router.post("/login", response_model=LoginResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user: User | None = await get_user_by_email(form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    if not await verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    access_token = create_access_token(
        data={"sub": str(user.id)},
        expires_delta=timedelta(minutes=30),
    )
    return LoginResponse(
        access_token=access_token,
        token_type="bearer"
    )

@router.post("/logout", response_model=LogoutResponse)
async def logout(token: str = Depends(oauth2_scheme)):
    await revoke_token(token)
    return LogoutResponse(message="Logged out successfully")

@router.get("/me", response_model=UserResponse)
async def me(current_user: User = Depends(get_current_user)):
    return current_user