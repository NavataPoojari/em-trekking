from sqlalchemy.orm import Session
from app.models.user_model import User


class UserRepository:

    def __init__(self):
        self.model = User


    def create_user(self, db: Session, user):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def get_all(self, db: Session):
        return db.query(User).all()

    def get_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()