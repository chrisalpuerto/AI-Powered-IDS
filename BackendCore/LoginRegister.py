'''
For now this file is used to register and login users.
in the future, can implement a more complex system, possibly using a database w/ SQL
'''

users = {}

def register_user(username, password):
    if username in users:
        print("Username already exists.")
        return False
    users[username] = password
    print("Registration successful.")
    return True