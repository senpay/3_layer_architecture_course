from business.exceptions import InvalidUserException, Unauthorized, UserNotFoundException
from business.model.role import ADMIN
from business.model.user import User
from business.user_validator import UserValidator
from persistance.inmemory_storage import InMemoryStorage

class UserService:
    
    def __init__(self, user_storage = None):
        if user_storage is None:
            self._user_storage = InMemoryStorage()
        else:
            self._user_storage = user_storage

        self._user_validator = UserValidator(self._user_storage)

    
    
    def create(self, user: User) -> int:
        if (not self._user_validator.validate(user)):
            raise InvalidUserException()
        return self._user_storage.add(user)
    
    def get(self, user_id: int, token = None) -> User:
        if token == None:
            raise Unauthorized('Token is required')
        
        auth_user = self.authenticate_user(token)
        if auth_user == None:
            raise Unauthorized('Invalid token')
        
        if auth_user.user_id != user_id and auth_user.role != ADMIN:
            raise Unauthorized('You can\'t access this user\'s data')

        user = self._user_storage.get(user_id)
        if user is None:
            raise UserNotFoundException()
        return user
    
    def update(self, user: User, token = None):
        if (not self.get(user.user_id)):
            raise UserNotFoundException()
        self._user_storage.update(user)

    def delete(self, user_id: int, token = None):
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
    
    def authenticate_user(self, token: str) -> User:
        return self._user_storage.find_by_token(token)
    
    def __generate_token(self):
        return '1234567890'