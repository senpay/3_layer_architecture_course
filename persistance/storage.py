from business.model.user import User


class UserStorage:

    def save(self, user: User) -> int:
        raise NotImplementedError()

    def get(self, user_id: int) -> User:
        raise NotImplementedError()

    def find_by_user_name(self, user_name: str) -> User:
        raise NotImplementedError()