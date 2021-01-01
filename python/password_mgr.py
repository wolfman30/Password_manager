import string 

letters = string.ascii_letters #reters to all English letters in lowercase and upper case in a string
numbers = list(range(0, 10)) #refers to all numbers from 0 to 9 in a list
special_chars = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''


class BasePasswordManager:

    #list holding all user's past passwords
    #last item of old_passwords is current password
    old_passwords = []

    try: 

        with open('passwords.txt', 'r') as passwords:
            for word in passwords.readlines(): 
                old_passwords.append(word)

    except: 
        pass
        
    def __str__(self):
        return "Your current password is {}".format(self.old_passwords[-1])

    def get_password(self):
        return self.old_passwords[-1]

    def is_correct(self, string):
        if string == self.old_passwords[-1]:
            return True
        else:
            return False


class PasswordManager(BasePasswordManager):

    def set_password(self):

        inp = input('Set your password: ')

        with open('passwords.txt', 'a+') as pwds: 
            pwds.write(inp + '\n')
       
        
        return self.old_passwords.append(inp)

    def get_level(self): 
        pass 



user = PasswordManager()
user.set_password()

print(user)

print(user.old_passwords)


