import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviors.

    Args:
        unittest.TestCase:helps in creating test cases
    '''
    def setUp(self):
        '''
        Function to create a user account before each test
        '''
        self.new_user = User('Dan', '1234')

    def test_init_(self):
        '''
        Test to if check the initialization/creation of user instances is properly done
        '''
        self.assertEqual(self.new_user.username, 'Dan')
        self.assertEqual(self.new_user.password, '1234')

    def test_save_user(self):
        '''
        Test to check if the new users info is saved into the users list
        '''
        self.new_user.save_User()
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
