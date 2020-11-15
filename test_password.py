import unittest
from password import User

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class.

    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Nadine","Nadine123") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Nadine")
        self.assertEqual(self.new_user.password,"Nadine123")



    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()