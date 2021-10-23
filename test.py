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
        self.assertEqual(len(User.user_list), 1)

    def test_delete_user(self):
        """
        check whether the user was removed from the user accounts list
        """
        self.assertEqual(len(User.user_list), 0)
        self.new_user.save_User()
        self.assertEqual(len(User.user_list), 1)
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 0)

    @classmethod
    def find_user(cls, username):
        """Find user by username"""
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def user_exist(cls, username):
        #Check if user exists
        for user in cls.user_list:
            if user.username == username:
                return True
            return False

    @classmethod
    def check_user(cls, username, password):
        """
        Check if user exists and if password is correct
        """
        user = cls.find_user(username)
        if user and user.password == password:
            return True
        return False



if __name__ == '__main__':
    unittest.main()
