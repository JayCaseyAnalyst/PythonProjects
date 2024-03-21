from cryptography.fernet import Fernet
import string
import random

def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

'''
def gen_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as file:
        file.write(key)
    
gen_key()
'''

letters = string.ascii_letters
chars = string.punctuation
chars = chars.replace("|", "")
nums = string.digits




def create_pass():
    web = input("Website?")
    user_name = input("Username/email?")
    length = int(input("Password Minimum Length?"))
    pw = ''

    lis = letters + chars + (nums*3)
        
    while len(pw) < length:
        new = random.choice(lis)
        pw += new
        
    with open('secretaccess.text', 'a') as file:
        file.write(web + '|' + user_name + '|' + fer.encrypt(pw.encode()).decode() + '\n')

    
    return pw

def view_pass():
    with open("secretaccess.text", 'r') as file:
            for line in file:
                data = line.rstrip()
                web, user, pw = data.split("|")
                print(web, " | ", user, " | ", fer.decrypt(pw.encode()).decode())



'''
def test1():
    website = input("what is this for?")
    user_name = input("Username/email?")
    pw = create_pass()

    pw2 = f.encrypt(pw)
    pw3 = f.decrypt(pw2)

    print(pw, pw2, pw3)
'''



while True:
    mode = input("Add new password or view existing? (add/view) q to quit")

    if mode == "q":
        break
    if mode == 'add':
        create_pass()
        pass
    elif mode == 'view':
        view_pass()
        pass


    

