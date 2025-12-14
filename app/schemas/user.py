from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    email: EmailStr = Field(None, example="test@example.com")

class UserCreate(UserBase):
    password: str = Field(None, min_length=8, example="password123")

class User(UserCreate):
    id: int
    class Config:
          from_attributes = True

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes = True
        
class UserUpdate(UserBase):
    email: EmailStr | None = Field(None, example="test@example.com")
    password: str | None = Field(None, min_length=8, example="password123")