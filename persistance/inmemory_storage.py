from persistance.storage import UserStorage


class InMemoryStorage(UserStorage):
    def __init__(self):
        self._data = []

    def get(self, user_id):
        if user_id is None or user_id >= len(self._data):
            return None
        return self._data[user_id]

    def add(self, user):
        user_id = len(self._data)
        user.user_id = user_id
        self._data.append(user)
        return user_id
    
    def delete(self, user_id):
        if user_id is None or user_id >= len(self._data):
            return
        self._data[user_id] = None

    def update(self, user):
        self._data[user.user_id] = user

    def find_by_user_name(self, user_name):
        for user in self._data:
            if user.user_name == user_name:
                return user
        return None
    
    def find_by_token(self, token):
        for user in self._data:
            if user.auth_token == token:
                return user
        return None