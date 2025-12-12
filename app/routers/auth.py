from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, UserCreateResponse, User
from app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/auth/login")

@router.post("/signup", response_model=UserCreateResponse)
async def signup(user_body: UserCreate):
    return UserCreateResponse(
        id=1,
        username=user_body.username,
        email=user_body.email,
        password=user_body.password
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

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    if token != "fake_token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    return User(
        id=1,
        username="YamadaTaro",
        email="test@example.com",
        password="password123"
    )

@router.get("/me", response_model=User)
async def me(current_user: User = Depends(get_current_user)):
    return current_user