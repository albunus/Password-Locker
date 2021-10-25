import pyperclip 
import random
import string

#Global Variables

global users_list
class User:
    '''
    Class to create user accounts and save their information 
    '''
    # Class variables
    #global users_list
    users_list = []
    def __init__(self, first_name, last_name,password):
        '''
        method to define the properties for each user objective will hold
        '''
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    
    def save_user(self):
        '''
        Function to save a newly created instance
        '''
        User.users_list.append(self)
class Credential:
    '''
    class to create account credentials, generate passwords and save their information
    '''
    # Class variables
    credentials_list =[]
    user_credentials_list =[]
    @classmethod
    def check_user (cls,first_name,password):
        '''
        Method that checks if the name and password entered matches the entries in users_list
        '''
        current_user =''
        for user in User.users_list:
            if (user.first_name ==first_name and user.password == password):
                current_user = user.first_name
            return current_user
    def __init__(self,user_name,nick_name,platform_name,password):
        '''
        Method to define if the properties for each user object will hold.
        '''

        #instance variables
        self.user_name = user_name
        self.nick_name = nick_name
        self.platform_name = platform_name
        self.password = password

    def save_credentials(self):
        '''
        Function to create a newly created user instance
        '''
        #global users_list
        Credential.credentials_list.append(self)

    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate an 8 character password for a credential
        '''
        gen_pass=''.join(random.choice(char)for _ in range(size))
        return gen_pass

    @classmethod
    def display_credentials(cls,user_name):
        '''
        Class method to display the list of credentials saved
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list

    @classmethod
    def find_by_nick_name(cls,nick_name):
        '''
        method that takes in a site name and returns a credential that matches that site name.
        '''
        for credential in cls.credentials_list:
            if credential.nick_name == nick_name:
                return credential
    @classmethod
    def copy_credential(cls,nick_name):
        '''
        Class method that copies a credentials information after the credentials site name is entered
        '''
        find_credential = Credential.find_by_nick_name(nick_name)
        return pyperclip.copy(find_credential.password)

