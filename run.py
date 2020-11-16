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
    elif short_code == "b":
        print("Login to your account")
        print('-'*50)
        print("login_username:")
        username = input()
        print("login_password:")
        password = input()
        login = login_user(username,password)
        print('\n')
        print(f"Hello {username}.Welcome To PassWord Locker Manager")  
        print("Choose between the following:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n DC - Delete credential \n EX - Exit the application \n")
        short_code=input("").lower().strip()
        if short_code == "cc":
            print("Creating a new credential")
            print('-'*50)
            print("Account Name ")
            accname = input().lower()
            print("Username ")
            userName = input()
            print("Password")
            password = input()
            save_credential(create_new_credential(accname,userName,password))
            print(f"Account Credential for: {accname} - UserName: {userName} - Password:{password} created succesfully")
            print("\n")
        elif short_code == "dc":
            print("Display Credentials")
        elif short_code == "fc":
            print("Finding Credentials")
        elif short_code == "dc":
            print("Deleting Credentials")
        elif short_code == "ex":
            print("Thanks for using password locker")
        else:
            print("Invalid")
        

              



if __name__ == '__main__':
    main()