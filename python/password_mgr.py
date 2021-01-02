import string 

letters = string.ascii_letters #reters to all English letters in lowercase and upper case in a string
numbers = "0123456789"
special_chars = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''


class BasePasswordManager:

    #list holding all user's past passwords
    #last item of old_passwords is current password
    old_passwords = []

    #initializes password user's input as a class variable
    password_input = None

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

        self.password_input = input('Set your password: ')

        while len(self.password_input) < 6:
            self.password_input = input("Your password need to be a minimum length of 6 characters. Try again: ")

        with open('passwords.txt', 'a+') as pwds: 
            pwds.write(self.password_input + '\n')
       
        
        return self.old_passwords.append(self.password_input)

    def get_level(self): 
        for letter in letters: 
            for num in numbers: 
                for char in special_chars: 
                    if letter in self.password_input and num in self.password_input and char in self.password_input: 
                        level_3 = True
                        print('Your new password meets security level 3 \n')
                        return level_3
        for char in self.password_input:
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

user.get_level()

print("Here are all your passwords, from earliest to latest:", user.old_passwords)


