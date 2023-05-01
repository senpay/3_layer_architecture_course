from business.exceptions import InvalidUserException, UserNotFoundException
from business.model.user import User
from business.user_validator import UserValidator
from persistance.inmemory_storage import InMemoryStorage
from persistance.sqlite_storage import SqliteStorage

class UserService:
    
    def __init__(self):
        # self._user_storage = InMemoryStorage()
        self._user_storage = SqliteStorage()
        self._user_validator = UserValidator(self._user_storage)
    
    def create(self, user: User) -> int:
        if (not self._user_validator.validate(user)):
            raise InvalidUserException()
        return self._user_storage.add(user)
    
    def get(self, user_id: int) -> User:
        user = self._user_storage.get(user_id)
        if user is None:
            raise UserNotFoundException()
        return user
    
    def update(self, user: User):
        if (not self.get(user.user_id)):
            raise UserNotFoundException()
        self._user_storage.update(user)

    def delete(self, user_id: int):
        if (not self.get(user_id)):
            raise UserNotFoundException()
        self._user_storage.delete(user_id)

    
    ## Authentication functionality implementation
    def authenticate(self, user_name: str) -> User:
        user = self._user_storage.find_by_user_name(user_name)
        if user is None:
            raise UserNotFoundException()
        
        if user.auth_token == None:
            user.auth_token = self.__generate_token() 
            self._user_storage.update(user)

        return user
    
    def __generate_token(self):
        return '1234567890'