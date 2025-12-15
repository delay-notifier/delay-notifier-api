from fastapi import APIRouter, Depends
import app.schemas.user as user_schema
from app.routers.auth import get_current_user

router = APIRouter()

@router.get("/me", response_model=user_schema.UserResponse)
async def get_me(current_user: user_schema.UserResponse = Depends(get_current_user)):
    return current_user

@router.get("/{user_id}", response_model=user_schema.UserResponse)
async def get_user(user_id: int):
    return user_schema.UserResponse(
        id=user_id,
        email="test@example.com"
    )

@router.get("", response_model=list[user_schema.UserResponse])
async def list_users():
    return [
        user_schema.UserResponse(
            id=1,
            email="test@example.com"
        ),
        user_schema.UserResponse(
            id=2,
            email="hanako@example.com"
        )
    ]

@router.post("", response_model=user_schema.UserResponse)
async def create_user(user_body: user_schema.UserCreate):
    return user_schema.UserResponse(
        id=1,
        email=user_body.email
    )

@router.put("/{user_id}", response_model=user_schema.UserResponse)
async def update_user(user_id: int, user_body: user_schema.UserUpdate):
    return user_schema.UserResponse(
        id=user_id,
        email=user_body.email
    )

@router.delete("/{user_id}", response_model=None)
async def delete_user(user_id: int):
    return {"message": f"User {user_id} deleted (dummy)" }