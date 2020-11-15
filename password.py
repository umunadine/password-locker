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

    def delete_credential(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Credentials.credential_list.remove(self)

    @classmethod
    def find_credential(cls,accname):
        '''
        Method that takes in an account_name and returns credentials that matches that name.

        '''

        for credential in cls.credential_list:
            if credential.accname == accname:
                return credential


    @classmethod
    def credential_exist(cls,accname):
        '''
        Method that checks if a credential exists from the credential list.
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for credential in cls.credential_list:
            if credential.accname == accname:
                    return True

        return False

    
      