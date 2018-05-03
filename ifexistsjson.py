import json

def get_stored_username_and_greet():
    """ get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username  = json.load(f_obj)
    except FileNotFoundError:
        username = input('What is the your username? ')
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print('Sup ' + username)
    else:
        print('Welcome back, ' + username)
            
get_stored_username_and_greet()