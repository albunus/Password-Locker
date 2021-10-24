class Credentials:
    '''
    A class tha generates users list credentials
    '''

    Accounts_details = []
    
    def _init_(self, social_platforms_accounts, user_account_username, user_account_password):
        '''
        initializing social platforms accounts
        '''
        self.social_platforms_accounts = social_platforms_accounts
        self.user_accounts_username = user_account_username
        self.user_accounts_password = user_account_password