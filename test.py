import unittest
from unittest.case import TestCase
from credentials import Credentials
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
        self.new_user = User('Dan','tush','tushy','1234')

    def test_init_(self):
        '''
        Test to if check the initialization/creation of user instances is properly done
        '''
        self.assertEqual(self.new_user.first_name, 'Dan')
        self.assertEqual(self.new_user.last_name, 'tush')
        self.assertEqual(self.new_user.username, 'tushy')
        self.assertEqual(self.new_user.password, '1234')

    def test_save_user(self):
        '''
        Test to check if the new users info is saved into the users list
        '''
        self.new_user.save_User()
        self.assertEqual(len(User.user_Accounts), 1)

    def test_delete_user(self):
        """
        check whether the user was removed from the user accounts list
        """
        self.assertEqual(len(User.user_Accounts), 0)
        self.new_user.save_User()
        self.assertEqual(len(User.user_Accounts), 1)
        self.new_user.delete_user()
        self.assertEqual(len(User.user_Accounts), 0)



    def test_find_user(self):
        """
        check whether the user exists in the user list
        """
        self.found_username = User.find_user("tushy")
    def test_user_exists(self):
            """
        check whether the user account exists in the user list
        """
            self.found_username = User.user_exist("tushy")

    def test_check_user(self):
        '''
        validate user accounts credentials
        '''
        self.check_user = User.check_user ("tushy","1234")

        # testing for the user class ends here



        # testing for the credentials class starts here

    class TestCredentials(unittest.TestCase):
          '''
    Test class that defines test cases for the credentials class behaviors.

    Args:
        unittest.TestCase:helps in creating test cases
    '''



if __name__ == '__main__':
    unittest.main()
