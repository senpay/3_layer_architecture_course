from business.model.user import User
from persistance.storage import UserStorage


class UserValidator:

    def __init__(self, storage: UserStorage):
        self._storage = storage
        

    def validate(self, user: User) -> bool:
        if user.user_name is None or user.user_name == '':
            return False
        if user.first_name is None or user.first_name == '':
            return False
        if self._storage.find_by_user_name(user.user_name):
            return False
        return True