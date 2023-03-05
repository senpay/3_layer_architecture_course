import unittest
from business.exceptions import InvalidUserException, UserNotFoundException
from business.model.user import User

from business.user_service import UserService

class UserServiceTest(unittest.TestCase):

    def setUp(self):
        self._user_service = UserService()


    def test_should_be_able_to_create_and_retrieve_user(self):
        user = User(
            user_name='test_user',
            first_name='Test',
            last_name='User'
        )

        user_id = self._user_service.create(user)

        retrieved_user = self._user_service.get(user_id)

        self.assertIsNotNone(user_id)
        self.assertIsNotNone(retrieved_user)

        self.assertEqual(user.user_name, retrieved_user.user_name)
        self.assertEqual(user.first_name, retrieved_user.first_name)
        self.assertEqual(user.last_name, retrieved_user.last_name)
        self.assertEqual(retrieved_user.user_id, user_id)

    def test_get_should_handle_none_user_id(self):
        with self.assertRaises(UserNotFoundException):
            self._user_service.get(None)

    def test_create_should_not_allow_empty_user_name(self):

        user = User(
            user_name=None,
            first_name='Test',
            last_name='User'
        )

        with self.assertRaises(InvalidUserException):
            self._user_service.create(user)

    def test_create_should_not_allow_empty_string_user_name(self):

        user = User(
            user_name='',
            first_name='Test',
            last_name='User'
        )

        with self.assertRaises(InvalidUserException):
            self._user_service.create(user)

    def test_create_should_not_allow_empty_string_first_name(self):

        user = User(
            user_name='user_name',
            first_name='',
            last_name='User'
        )

        with self.assertRaises(InvalidUserException):
            self._user_service.create(user)

    def test_create_should_not_allow_empty_first_name(self):

        user = User(
            user_name='user_name',
            first_name=None,
            last_name='User'
        )

        with self.assertRaises(InvalidUserException):
            self._user_service.create(user)

    def test_create_should_not_allow_non_unique_user_name(self):

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

        user_id = self._user_service.create(user1)

        with self.assertRaises(InvalidUserException):
            self._user_service.create(user2)

    def test_should_be_able_to_delete_user(self):

        user = User(
            user_name='test_user',
            first_name='Test',
            last_name='User'
        )

        user_id = self._user_service.create(user)

        self._user_service.delete(user_id)

        with self.assertRaises(UserNotFoundException):
            self._user_service.get(user_id)

    def test_delete_should_handle_none_user_id(self):

        with self.assertRaises(UserNotFoundException):
            self._user_service.delete(None)

    def test_delete_should_handle_incorrect_user_id(self):
        incorrect_id = 12356

        with self.assertRaises(UserNotFoundException):
            self._user_service.delete(incorrect_id)

    def test_should_be_able_to_update_user(self):
        user = User(
            user_name='test_user',
            first_name='Test',
            last_name='User'
        )

        user_id = self._user_service.create(user)

        user.user_id = user_id
        user.first_name = 'Test1'
        user.last_name = 'User1'

        self._user_service.update(user)

        retrieved_user = self._user_service.get(user_id)

        self.assertEqual(user.first_name, retrieved_user.first_name)
        self.assertEqual(user.last_name, retrieved_user.last_name)

    def test_update_should_handle_none_user_id(self):
        user = User(
            user_name='test_user',
            first_name='Test',
            last_name='User'
        )

        with self.assertRaises(UserNotFoundException):
            self._user_service.update(user)

    def test_update_should_handle_incorrect_user_id(self):

        user = User(
            user_name='test_user',
            first_name='Test',
            last_name='User'
        )

        user.user_id = 12345

        with self.assertRaises(UserNotFoundException):
            self._user_service.update(user)

        
            
if __name__ == '__main__':
    unittest.main()