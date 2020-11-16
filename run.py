#!/usr/bin/env python3.6
from password import User
from password import Credentials


def create_new_user(username,password):
    '''
    Function to create a new user 
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a contact
    '''
    user.delete_user()

def create_new_credential(accname,userName,password):
    '''
    Function to create a new user 
    '''
    new_credential = Credentials(accname, userName, password)
    return new_credential

def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credentials.verify_user(username,password)
    return check_user

def save_credential(credentials):
    '''
    Function to save a new user
    '''
    credentials.save_credential()
def delete_credential(credentials):
    '''
    Function to save a new user
    '''
    credentials.delete_credential()

def find_credential(credentials):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credentials.find_credential(accname)

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()

def check_existing_credential(accname):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credentials.credential_exist(accname)

def display_credentials():
    '''
    Function that returns all the saved contacts
    '''
    return Credentials.display_credentials()

def main():
    print("Hello Welcome to Password Locker...\n Please enter one of the following to proceed.\n A ---  Sign Up  \n B ---  Login  \n")
    short_code=input("").lower().strip()
    if short_code == "a":
        print("Creating a new account")
        print('-' * 50)
        print("User_name:")
        username = input()
        print("Enter Password")
        password = input()
        save_user(create_new_user(username,password))
        print('-' * 50)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
    
              



if __name__ == '__main__':
    main()