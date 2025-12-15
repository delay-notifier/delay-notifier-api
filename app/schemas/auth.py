from pydantic import BaseModel, EmailStr, Field

class LoginBase(BaseModel):
    email: EmailStr = Field(None, example="test@example.com")
    password: str = Field(None, min_length=8, example="password123")

class LoginRequest(LoginBase):
    pass

class LoginResponse(BaseModel):
    access_token: str = Field(None, description="JWT アクセストークン")
    token_type: str = Field("bearer", description="トークンタイプ（通常は bearer）")

    class Config:
        orm_mode = True

class TokenData(LoginBase):
    user_id: int | None = Field(None, description="JWT 内のユーザーID")

    class Config:
        orm_mode = True

class LogoutResponse(LoginBase):
    message: str = Field("Logged out successfully", example="Logged out successfully")

    class Config:
        orm_mode = True
