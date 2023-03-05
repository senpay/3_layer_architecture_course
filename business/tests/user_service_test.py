import unittest
from business.exceptions import InvalidUserException, UserNotFoundException
from business.model.user import User

from business.user_service import UserService

class UserServiceTest(unittest.TestCase):

    def test_should_be_able_to_create_and_retrieve_user(self):
        user_service = UserService()

        user = User(
            user_name='test_user',
            first_name='Test',
            last_name='User'
        )

        user_id = user_service.create(user)
        retrieved_user = user_service.get(user_id)

        self.assertIsNotNone(user_id)
        self.assertIsNotNone(retrieved_user)

        self.assertEqual(user.user_name, retrieved_user.user_name)
        self.assertEqual(user.first_name, retrieved_user.first_name)
        self.assertEqual(user.last_name, retrieved_user.last_name)
        self.assertEqual(retrieved_user.user_id, user_id)

    def test_get_should_handle_none_user_id(self):
        user_service = UserService()

        with self.assertRaises(UserNotFoundException):
            user_service.get(None)

    def test_create_should_not_allow_empty_user_name(self):
        user_service = UserService()

        user = User(
            user_name=None,
            first_name='Test',
            last_name='User'
        )

        with self.assertRaises(InvalidUserException):
            user_service.create(user)

    def test_create_should_not_allow_empty_string_user_name(self):
        user_service = UserService()

        user = User(
            user_name='',
            first_name='Test',
            last_name='User'
        )

        with self.assertRaises(InvalidUserException):
            user_service.create(user)

    def test_create_should_not_allow_empty_string_first_name(self):
        user_service = UserService()

        user = User(
            user_name='user_name',
            first_name='',
            last_name='User'
        )

        with self.assertRaises(InvalidUserException):
            user_service.create(user)

    def test_create_should_not_allow_empty_first_name(self):
        user_service = UserService()

        user = User(
            user_name='user_name',
            first_name=None,
            last_name='User'
        )

        with self.assertRaises(InvalidUserException):
            user_service.create(user)

    def test_create_should_not_allow_non_unique_user_name(self):
        user_service = UserService()

        user1 = User(
            user_name='user_name',
            first_name='Test',
            last_name='User'
        )

        user2 = User(
            user_name='user_name',
            first_name='Test1',
            last_name='User1'
        )

        user_service.create(user1)

        with self.assertRaises(InvalidUserException):
            user_service.create(user2)
            
if __name__ == '__main__':
    unittest.main()