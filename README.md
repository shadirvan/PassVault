# PASSVAULT
## Why You Need PassVault :
It is not safe to use same passwords for all your accounts.
But it is also hard to remember different passwords for all accounts.
pass vault comes to the rescue. With passvault you can save all passwords in your own device without the fear of forgetting it.
passvault utilise the cryptography python module to encrypt passwords so that only you can access the encrypted password with a key.
This is my first official script . Your support mean world to me.

## PassVault Menu :
- Save a Password
- Encrypt Password
- Decrypt Password
- View Saved Passwords
- Quit Program
## How to install on linux :
you might need python and other development libraries for installing cryptography module.
install it by the following command in terminal.</br>

For Debian :</br>

`sudo apt-get install build-essential libssl-dev libffi-dev python-dev ` </br>

For Fedora and RHEL-derivatives :

`sudo yum install gcc libffi-devel python-devel OpenSSL-devel`

Make sure python is installed in your pc.

Now clone passvault into your device :

`git clone https://github.com/shadirvan/PassVault.git`

`cd PassVault`

`pip install -r requirements.txt`

`python3 PassVault.py`

## How to install on termux:
You need to install several package for the proper working of the script. install them by the following command:</br>

`pkg install python python3 python3-pip clang libcrypt libffi git`

Since most device running termux are aarch you need a few setups enter the following commands:

`rust --print target-list`

if your device is aarch64 run following else skip the step

`export CARGO_BUILD_TARGET=aarch64-linux-android`

Now You need to clone to script directory using following command :

`git clone https://github.com/shadirvan/PassVault.git`

`cd PassVault`

`pip install -r requirements.txt`

`python3 PassVault.py`

## How to use
When you install and run program it will open the menu. In the menu first you need to add attest one password. by using the option save a password and follow the instruction.
After that choose to encrypt password option to encrypt the saved password. It will ask for a key enter a key you like. remember the key
you need it for decrypting the passwords. Once you encrypted you can safely quit the program. For decrypting run the program and choose decrypt it will ask for the key. enter the key you used for encryption. and it will do the magic . inorder to see the save passwords
choose the view password option after decrypt. 

Note : Use the same key for decrypting otherwise the program might crash.
