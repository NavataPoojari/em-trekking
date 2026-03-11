from abc import ABC, abstractmethod


class UserService(ABC):

    @abstractmethod
    def create_user(self, db, user):
        pass

    @abstractmethod
    def get_users(self, db):
        pass