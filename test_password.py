import unittest
from password import User
from password import Credentials

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class.

    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Nadine","QwErtY") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Nadine")
        self.assertEqual(self.new_user.password,"QwErtY")



    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)
    
class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("Instagram","Nadine","AbcD12") # create credential object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.accname,"Instagram")
        self.assertEqual(self.new_credential.userName,"Nadine")
        self.assertEqual(self.new_credential.password,"AbcD12")

    def test_save_credential(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_credential.save_credential() # saving the new contact
        self.assertEqual(len(Credentials.credential_list),1)





if __name__ == '__main__':
    unittest.main()