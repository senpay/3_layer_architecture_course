from business.model.user import User


class UserController:

    def __init__(self, user_service):
        self.user_service = user_service

    def create_user(self, incoming_data):
        user = User(
            incoming_data.get('user_name', None),
            incoming_data.get('first_name', None),
            incoming_data.get('last_name', None)
        )
        user_id = self.user_service.create(user)
        user.user_id = user_id
        return user.__dict__

    # Updated to consume token
    def get_user(self, user_id, authorization_header):
        #Bearer token
        token = (authorization_header.replace('Bearer ', '')
                 if authorization_header else None)
        user_id_int = fault_safe_to_int(user_id)
        user = self.user_service.get(user_id_int, token)
        return user.__dict__

    # Really simple authentication controller
    def authenticate(self, incoming_data):
        user = self.user_service.authenticate(incoming_data.get('user_name', None))
        return user.__dict__

def fault_safe_to_int(user_id):
    try:
        return int(user_id)
    except:
        return None