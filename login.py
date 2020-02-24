# login system checker attempt
# Connor Campbell 24/02/2020

# import needed libraries
import hashlib

# get an initial username from the user
def get_user():
    global user_name
    global real_hash
    global salt
    
    found = False
    with open("user_creds.txt", "r") as file:
        for line in file:
            line = line.strip()
            details = line.split(":")
            # if there is a match then make found True
            if details[0] == user_name:
                found = True
                salt = details[1]
                real_hash = details[2]
    # if found is not true then ask for another username from the user and re run the check_name function
    if found != True:
        user_name = input("User not found, please re-enter username: ")
        get_user()

    return user_name
# get a password from the user
def get_pass():
    global user_name
    global salt
    global real_hash
    global x

    # get password entry attempt from user and create a hash using the password the user has given me
    user_pass = input("Please enter the password associated with " + user_name + ":")
    guess_hash = hashlib.sha256(user_pass.encode() + salt.encode()).hexdigest()

    # compare the new hash and the real hash
    if guess_hash == real_hash:
        # if they match then grant access
        print("Access granted!")
    # if hashes dont match, give user another attempt (3 total)
    elif x > 0:
        print("Incorrect password. Attempts remaining: ", x)
        # countdown to denying access
        x = x - 1
        get_pass()
    else:
        # if all attmepts are gone and hashes still dont match then deny access and end program
        print("Access Denied!")
        print("Exiting...")
        
# main program
user_name = ""
user_name = input("Username: ")
get_user()
print("User found!")
# x is used to countdown password entry attempts
x = 3
get_pass()

    
