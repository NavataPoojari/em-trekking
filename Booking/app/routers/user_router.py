from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserResponse
from app.serviceImpl.user_service_impl import UserServiceImpl

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

service = UserServiceImpl(user_repo=UserRepository())


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return service.get_users(db)