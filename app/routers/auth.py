from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, UserResponse, User
from app.schemas.auth import LoginResponse
from app.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
async def signup(user_body: UserCreate):
    return UserResponse(
        id=1,
        email=user_body.email
    )

@router.post("/login", response_model=LoginResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return LoginResponse(
        access_token="fake_token",
        token_type="bearer"
    )

@router.post("/logout")
async def logout():
    return {"message": "Logged out (dummy)"}

@router.get("/me", response_model=UserResponse)
async def me(current_user: User = Depends(get_current_user)):
    return current_user