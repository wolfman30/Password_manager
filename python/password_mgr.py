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
                word = word.strip()
                old_passwords.append(word)

    except: 
        pass
        
    def __str__(self):
        return "\nYour current password is {}\n".format(self.old_passwords[-1])

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

        while len(inp) < 6:
            inp = input("Your password need to be a minimum length of 6 characters. Try again: ")

        with open('passwords.txt', 'a+') as pwds: 
            pwds.write(inp + '\n')
       
        
        return self.old_passwords.append(inp)

    def get_level(self): 
        pass 



user = PasswordManager()

while True: 
    if user.old_passwords != []: 
        user_y_n = input('You already have a password. Do you want to set another one? y for yes, n for no ').lower()
        while user_y_n not in ['y', 'n']: 
            user_y_n = input("Sorry, did not understand. Type a y for yes or an n for no.")
        if user_y_n == 'y':
            user.set_password()
            user_y_n = input('Are you satisfied with this password? y for yes, n for no ')
            if user_y_n == 'y':
                break
            else: 
                continue
        else: 
            break

print(user)

print("Here are all your passwords, from earliest to latest:", user.old_passwords)


