from business.model.role import REGULAR


class User:

    def __init__(self, user_name, first_name, last_name):
        self.user_id = None
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.role = REGULAR
