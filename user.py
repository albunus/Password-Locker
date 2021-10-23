class User:
    '''
    class to create user accounts and save their information
    '''
    user_list=[]

    def __init__(self, first_name, last_name, username, password):
        """
        Initialize the user.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save_User(self):
        '''
        Function to save a newly created instance
        '''
        User.user_list.append(self)
    def delete_user(self):
        '''
        Delete user from the list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_user(cls, username):
        """Find user by username"""
        for user in cls.user_list:
            if user.username == username:
                return username
    @classmethod
    def user_exist(cls, username):
        """Check if user exists"""
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


