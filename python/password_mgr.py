class BasePasswordManager:

    #list holding all user's past passwords
    #last item of old_passwords is current password
    old_passwords = [] 

    def get_password(self):
        return old_passwords[-1]

    def is_correct(self, string):
        if string == old_passwords[-1]:
            return True
        else:
            return False


class PasswordManager(BasePasswordManager):
    def set_password(self):
        pass

    def get_level(self): 
        pass 