
import random
import string


class Credentials():
    '''
    A class tha generates users list credentials
    '''

    platform_details = [];

    def __init__(self, social_platforms_accounts, user_account_username, user_account_password):
        '''
        initializing social platforms accounts
        '''
        self.social_platforms_accounts = social_platforms_accounts
        self.user_accounts_username = user_account_username
        self.user_accounts_password = user_account_password

    def save_credentials(self):
        '''
        method to save platform details
        '''
        Credentials.platform_details.append(self)

    def delete_credentials(self):
        '''
        method that will delete platforms details
        '''
        Credentials.platform_details.remove(self)

    @classmethod
    def find_by_social_platform_account(cls, social_platform_account):
        '''
            Method that takes in a account_platform and returns a credentials that matches that account_platform.
        '''
        for details in cls.platform_details:
            if details.social_platform_account == social_platform_account:
                return details
        return False

    @classmethod
    def display_credentials(cls):
        """
            returns the credentials list(all credentials)
        """
        return cls.platform_details
    @classmethod
    def generate_password(cls, password_length):
        """
        generate random password for a user creating a new account int the user_credentials[]
        """
        tush = string.ascii_letters + string.digits
        password = ''.join(random.choice(tush)
                        for i in range(password_length))
        return password



