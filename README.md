## Password-locker
## Built By albunus mutuku
## Description
- Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.
## User Stories
- These are the behaviours/features that the application implements for use by a user.
- As a user I would like:
- To create an account with my details - log in with password
- Store my existing login credentials
- Generate a password for a new credential/account
- Copy my credentials to the clipboard
## Specifications
## Behaviour,Input& Output
- Display codes for navigation  In terminal: $./password_locker.py  Welcome, choose an option: cc-Create Account, lg-Log In, ex-Exit
- Display prompt for creating an account  Enter: ca Enter your first name, last name and password
- Display prompt for login in Enter: lg Enter your account name and password
- Display codes for navigation  Successful login  Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit
- Display prompt for creating a credential  Enter: cc Enter the nick name, your username and password
- Display a list of credentials Enter: dc Prints a list of saved credentials
- Display prompt for which credential to copy Enter: copy Enter the nick name of the credential you wish to copy.
- Exit application  Enter: ex Exit the current navigation stage
## SetUp / Installation Requirements
-desktop/laptop/device with operating system most appropriate linux
- python3
- pip
- pyperclip
## In your terminal:
  - $ git clone https://github.com/albunus/Password-Locker
  - $ cd Password-locker
  - Running the Application
  - To run the application, in your terminal:
  - $ chmod +x run.py
  - $ ./run.py
  - Testing the Application
  - To run the tests for the class file:
  - $ python3 test.py
## Technologies Used
  - Python3.8

MIT License

Copyright (c) 2021 Albunus

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.




