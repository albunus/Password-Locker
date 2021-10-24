import unittest
from user import User
from credentials import Credentials


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
    def setUp(self):
        '''
        function to have social platforms details before testing
        '''
        self.new_credentials = Credentials('twitter','aly','tush')
    def test__init__(self):
        '''
        test to see whether the credentials are created
        '''
        self.assertEqual(self.new_credentials.social_platforms_accounts, 'twitter')
        self.assertEqual(self.new_credentials.user_accounts_username, 'aly')
        self.assertEqual(self.new_credentials.user_accounts_password, 'tush')

    def test_save_credentials(self):
        '''
        confirm whether platform details are being saved
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.platform_details),1)

    def test_delete_credentials(self):
        '''
        confirm whether platforms deatails are being deleted from the saved list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.platform_details),1)
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.platform_details),0)

    def test_find_credentials_by_social_platform_account(self):
        '''
        testing finding method
        '''
        self.found_credentials = Credentials.find_by_social_platform_account,("twitter")

    def test_display_all_credentials(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.platform_details)



if __name__ == '__main__':
    unittest.main()
