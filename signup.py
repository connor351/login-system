# Sign up program
# Connor Campbell 24/02/2020

# import libraries needed
import random
import hashlib

# get username and password from user
user_name = input("Please enter a username: ")
user_pass = input("Please enter a password: ")

# create a random salt generator
# SJ: If you import string, you can use ascii_lowercase etc.
salt_list = ['A', 'B', 'C', 'X', 'Y', 'Z', '1', '2', '3', '8', '9', '0']
salt = "".join([random.choice(salt_list) for _ in range (0, 64)])

# hash the user_pass using sha-256, remember to enconde and add salt(also encoded) and remember to digest the object
hash_pass = hashlib.sha256(user_pass.encode() + salt.encode()).hexdigest()

with open("user_creds.txt", "a") as file:
    file.write("\n" + user_name + ":" + salt + ":" + hash_pass)

