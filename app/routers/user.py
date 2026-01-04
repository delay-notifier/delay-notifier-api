from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import app.schemas.user as user_schema
from app.database import get_db
from app.crud import user as user_crud
from app.dependencies.auth import get_current_user

router = APIRouter()


@router.get("/me", response_model=user_schema.UserResponse)
async def get_me(current_user: user_schema.UserResponse = Depends(get_current_user)):
    return current_user


@router.get("/{user_id}", response_model=user_schema.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    return db_user


@router.get("", response_model=list[user_schema.User])
async def list_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users


@router.post(
    "",
    response_model=user_schema.UserCreateResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    user_body: user_schema.UserCreate,
    db: Session = Depends(get_db)
):

    db_user = user_crud.get_user_by_email(db, email=user_body.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    db_user = user_crud.get_user_by_username(db, username=user_body.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )

    return user_crud.create_user(db, user=user_body)


@router.put("/{user_id}", response_model=user_schema.User)
async def update_user(
    user_id: int,
    user_body: user_schema.UserUpdate,
    db: Session = Depends(get_db)
):
    if user_body.email:
        db_user = user_crud.get_user_by_email(db, email=user_body.email)
        if db_user and db_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

    if user_body.username:
        db_user = user_crud.get_user_by_username(db, username=user_body.username)
        if db_user and db_user.id != user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken"
            )

    db_user = user_crud.update_user(db, user_id=user_id, user=user_body)

    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    return db_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    success = user_crud.delete_user(db, user_id=user_id)

    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    return None
