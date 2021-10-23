class User:
    '''
    class to create user accounts and save their information
    '''
    user_list=[]

    def __init__(self,username,password):
        '''
        method to define the properties for each user objective will hold
        '''
        #instance variables
        self.username = username
        self.password = password

    def save_User(self):
        '''
        Function to save a newly created instance
        '''
        User.user_list.append(self)