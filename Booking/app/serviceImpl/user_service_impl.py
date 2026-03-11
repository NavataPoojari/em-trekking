from sqlalchemy.testing.suite.test_reflection import users

from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.models.user_model import User
from app.utils.password_handler import hash_password



class UserServiceImpl(UserService):
    def __init__(self, user_repo : UserRepository):
        self.repo = user_repo

    def create_user(self, db, user):

        hashed = hash_password(user.password)

        db_user = User(
            name=user.name,
            email=user.email,
            password=hashed,
            phone=user.phone
        )

        return self.repo.create_user(db, db_user)

    def get_users(self, db):
        return self.repo.get_all(db)