from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from pydantic.types import conint
from decouple import config

# ============== user =================
class UserBase(BaseModel):
    email: EmailStr
    password: str
    is_active: bool # account is active or not
    is_superuser: bool
    is_staff: bool
    is_verified: bool # email verification

    class Config:
        orm_mode = True
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
        from_attributes = True


class Response(BaseModel):
    email: EmailStr
    created_at: datetime

class UserResp(BaseModel):
    User: List[Response]

    class Config:
        orm_mode = True

# ====================  Token  ====================
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None