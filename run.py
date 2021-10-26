#! /usr/bin/env python3
import pyperclip
from user import User, Credential

def create_user(fname,lname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user

def save_user(user):
    '''
	Function to save a new user account
	'''
    User.save_user(user)


def verify_user(first_name,password):
	'''
	Function that verifies the existence of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(user_name,nick_name,platform_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(user_name,nick_name,platform_name,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def display_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(user_name)
	
def copy_credential(nick_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(nick_name)

def main():
	print(' ')
	print(f'Hello! 😃😃Welcome to Password Locker.😃😃😃😃😃😃😃😃😃😃😃')
	while True:
		print(' ')
		print("-"*60)
		print('Use these codes to navigate: \n cc-Create an Account \n lg-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'cc':
			print("-"*60)
			print(' ')
			print('To create a new account:')
			first_name = input('Enter your first name - ').strip()
			last_name = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f'New Account Created for: {first_name}😃😃 {last_name} 😃😃using password: {password}😃😃 now login to proceed' )
		elif short_code == 'lg':
			print("-"*60)
			print(' ')
			print('To login, enter your account details:')
			user_name = input('Enter your first name - ').strip()
			password = str(input('Enter your password - '))
			user_exists = verify_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome😃 {user_name}.😃😃😃😃 Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n del-delete \n  ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {user_name}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your credential details:')
						nick_name = input('Enter the platform nick\'s name- eg fb  ').strip()
						platform_name = input('Enter your platform\'s name - eg facebook  ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose an option for entering a password: \n 1- create your password  \n 2-generate a password \n ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == '1':
								print(" ")
								password = input('Enter your password: 😃😃').strip()
								break
							elif psw_choice == '2':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Oops! Wrong option entered. Try again. 😥  😥 ')
						save_credential(create_credential(user_name,nick_name,platform_name,password))
						print(' ')
						print(f'Credential Created: nick Name: {nick_name} - platform Name: {platform_name} - Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_credentials(user_name):
							print('Here is a list of all your credentials')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'platform nick Name: {credential.nick_name} 😃- platform Name: {credential.platform_name} 😃- Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet  😥 😥 ")
							print(' ')
					elif short_code == "del":
            					print("Enter the account name of the Credentials you want to delete")
            					check_user = input().lower()
            					if check_user(save_credential):
               			 			check_credential = check_user(save_credential) 
						
					elif short_code == 'copy':
						print(' ')
						chosen_nick = input('Enter the platform nick name for the credential password to copy: ')
						copy_credential(chosen_nick)
						print('')

					else:
						print('Oops! Wrong option entered. Try again. 😥 ')

			else:
				print(' ')
				print('Oops! Wrong details entered. Try again or Create an Account. 😥 ')

		else:
			print("-"*60)
			print(' ')
			print('Oops! Wrong option entered. Try again. 😥 ')








if __name__ == '__main__':
	main()