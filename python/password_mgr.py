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
        
        return False


class PasswordManager(BasePasswordManager):

    def set_password(self):

        self.password_input = input('Set your password: ')

        while len(self.password_input) < 6 or self.get_level(password=self.password_input) <= self.get_level(self.old_passwords[-1]):
            
            if len(self.password_input) < 6: 
                self.password_input = input("Your password needs to be a minimum length of 6 characters. Try again: ")
            
            if self.get_level(password=self.password_input) <= self.get_level(self.old_passwords[-1]):
                self.password_input = input('The new password you typed does not meet the requirments of a security level greater than your last password. Try again: ')

        with open('passwords.txt', 'a+') as pwds: 
            pwds.write(self.password_input + '\n')
       
        
        return self.old_passwords.append(self.password_input)

    def get_level(self, password):

        letter_count = 0 
        num_count = 0 
        char_count = 0
        
        for char in password:
            if char in letters: 
                letter_count += 1 
            elif char in numbers: 
                num_count += 1
            elif char in special_chars: 
                char_count += 1 

        if char_count == 0: 
            if (letter_count >= 1 and num_count == 0) or (letter_count == 0 and num_count >= 1):
                level_0 = 0
                return level_0

            elif letter_count >= 1 and num_count >= 1:
                level_1 = 1
                return level_1
        else: 
            if letter_count >= 1 and num_count >= 1:
                level_2 = 2
                return level_2
                    



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


