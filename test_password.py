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

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credential_list = [] 


    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credentials("Facebook","tess","Opp12") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_contact(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_credential.save_credential()
            test_credential = Credentials("Facebook","tess","Opp12") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credentials.credential_list),1)

    
    def test_find_credentials(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential.save_credential()
        test_credential = Credentials("Facebook","tess","Opp12") 
        test_credential.save_credential()

        the_credential = Credentials.find_credential("Facebook")

        self.assertEqual(the_credential.accname,test_credential.accname)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credentials("Facebook","tess","Opp12") 
        test_credential.save_credential()

        credential_exists = Credentials.credential_exist("Facebook")

        self.assertTrue(credential_exists)

      

    def test_display_all_credential(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credential_list)

    

  

        

            





if __name__ == '__main__':
    unittest.main()