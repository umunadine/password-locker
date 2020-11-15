class User:
    """
    Class that generates new instances of user.
    """
    
    user_list = [] # Empty user list

    def __init__(self,username,password):
        self.username = username
        self.password = password


    def save_user(self):
       
        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

class Credentials:  

    credential_list = [] # Empty user list 

    def __init__(self,accname,userName, password):
        """
        user credentials to be stored
        """
        self.accname = accname
        self.userName = userName
        self.password = password

    def save_credential(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Credentials.credential_list.append(self)

    
      