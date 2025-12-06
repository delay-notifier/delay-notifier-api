from fastapi import APIRouter, Depends
import app.schemas.user as user_schema 

router = APIRouter()

@router.get("/{user_id}", response_model=user_schema.User)
async def get_user(user_id: int):
    return user_schema.User(
        id=user_id,
        username="YamadaTaro",
        email="test@example.com",
        password="password123"
    )

@router.get("", response_model=list[user_schema.User])
async def list_users():
    return [
        user_schema.User(
            id=1, username="YamadaTaro",
            email="test@example.com",
            password="password123"
        ),
        user_schema.User(
            id=2, 
            username="SuzukiHanako",
            email="hanako@example.com",
            password="password456"
        )
    ]

@router.post("", response_model=user_schema.UserCreateResponse)
async def create_user(user_body: user_schema.UserCreate):
    return user_schema.UserCreateResponse(id=1, **user_body.dict())

@router.put("/{user_id}", response_model=
            user_schema.UserCreateResponse)
async def update_user(user_id: int, user_body: user_schema.UserCreate):
    return user_schema.UserCreateResponse(id=user_id, **user_body.dict())

@router.delete("/{user_id}", response_model=None)
async def delete_user(user_id: int):
    return