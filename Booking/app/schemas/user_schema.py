from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str

    class Config:
        orm_mode = True