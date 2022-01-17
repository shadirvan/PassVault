
# IF YOU ARE MODIFYING THE PROGRAM PLEASE MENTION MY NAME. THIS PROGRAM TAKE A LOT OF TIME TO WRITE(I AM A BEGINNER)
import os
import sys
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def input_key():
    key = input("Enter key : ")
    key_byte = key.encode()
    return key_byte


def generate_salt():
    with open('.salt', 'wb') as salt_file:
        salt_file.write(os.urandom(16))


def salt_read():
    with open('.salt', 'rb') as salt_file:
        salt = salt_file.read()
    kdfvar = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=390000, )
    return kdfvar


def real_key(key_byte, kdf):
    realkey = base64.urlsafe_b64encode(kdf.derive(key_byte))
    return realkey


def encrypt_file(realkey):
    f = Fernet(realkey)
    with open('.pass.txt', 'rb') as file:
        original = file.read()
    encrypted = f.encrypt(original)

    with open('.pass.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print("Passwords Successfully Encrypted!")


def decrypt_file(realkey):
    f = Fernet(realkey)
    with open('.pass.txt', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = f.decrypt(encrypted)
    with open('.pass.txt', 'wb') as dec_file:
        dec_file.write(decrypted)
    print("Passwords Successfully Decrypted!")


def encryption_check():
    text = "Decrypted"
    flag = 0
    if file_check():
        file = open('.pass.txt', 'r')
        for line in file:
            if text in line:
                flag = 1
        if flag == 1:
            return False
        else:
            return True


def file_check():
    if os.path.isfile('.pass.txt'):
        return True
    else:
        return False


def salt_check():
    return os.path.isfile('./.salt')


def add_pass():
    username = input("Enter Username or Email : ")
    newpass = input("Enter the password : ")
    service = input("Enter the website or service : ")
    if os.path.isfile('./.pass.txt'):
        with open('.pass.txt', 'a') as pass_file:
            pass_file.write("[" + service + "]")

            pass_file.write('\n')
            pass_file.write('username :' + username)
            pass_file.write(' Password :' + newpass + " ")
            pass_file.write('\n')
    else:
        pass_file = open('.pass.txt', 'w+')
        pass_file.write('Decrypted')
        pass_file.write('\n')
        pass_file.write("[" + service + "]")
        pass_file.write('\n')
        pass_file.write('username :' + username)
        pass_file.write(' Password :' + newpass + " ")
        pass_file.write('\n')
    print("Password Added Successfully!")


def view_pass():
    if file_check():
        if encryption_check():
            print("Please Decrypt First!")
        else:
            with open('.pass.txt', 'rb') as file:
                for line in file:
                    print(line.decode())
    else:
        print("Save Least One Password")


choice = "shadirvan"
if not salt_check():
    generate_salt()
print("""
╔═══╗────────────────────╔╗╔╗──╔╗────╔╗╔╗
║╔═╗║────────────────────║║║╚╗╔╝║────║╠╝╚╗
║╚═╝╠══╦══╦══╦╗╔╗╔╦══╦═╦═╝║╚╗║║╔╩═╦╗╔╣╠╗╔╝
║╔══╣╔╗║══╣══╣╚╝╚╝║╔╗║╔╣╔╗║─║╚╝║╔╗║║║║║║║
║║──║╔╗╠══╠══╠╗╔╗╔╣╚╝║║║╚╝║─╚╗╔╣╔╗║╚╝║╚╣╚╗
╚╝──╚╝╚╩══╩══╝╚╝╚╝╚══╩╝╚══╝──╚╝╚╝╚╩══╩═╩═╝
                             by shadirvan
        """)
while choice == "shadirvan":

    user_choice = input(""" 
    1. Save A Password
    2. Encrypt Passwords
    3. Decrypt Passwords
    4. View All Saved Passwords
    5. Quit The Program
    Enter Your Choice : """)

    if user_choice == "2":
        if file_check():
            if encryption_check():
                print("File Already Encrypted")
            else:
                key_input = input_key()
                kdf = salt_read()
                realkey = real_key(key_input, kdf)
                encrypt_file(realkey)
        else:
            print('Save Least  One password')



    elif user_choice == "3":
        if not encryption_check():
            print(" File is Already Decrypted")
        else:

            key_input = input_key()
            kdf = salt_read()
            realkey = real_key(key_input, kdf)
            decrypt_file(realkey)

    elif user_choice == "1":
        if encryption_check():
            print("Please Decrypt First !")
        else:
            add_pass()


    elif user_choice == "4":
        view_pass()
    elif user_choice == "5":
        sys.exit("""Your support means world to me. 
Thank You for using the password Vault.
Developer : Shadirvan""")

    else:
        print("Please Enter a valid Choice")
