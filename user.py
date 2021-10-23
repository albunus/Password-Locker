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

    def test_find_user(self):
        """
        check whether the user account exists in the user list
        """
        self.found_user = User.find_user("tushy")

    def test_user_exists(self):
        """
        check whether the user account exists in the user list
        """
        self.found_user = User.user_exist("tushy")

