from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None

def get_new_user(path):
    """Prompt for a new user."""
    user = {}
    username = input('What is your name? ')
    password = input('Enter a password: ')
    office_location = input('Enter your office number: ')
    user['username'] = username
    user['password'] = password
    user['office number'] = office_location
    contents = json.dumps(user)
    path.write_text(contents)
    return username


def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        diff_user = input(f'Are you {username}?\nEnter y/n: ')
        if diff_user == 'n':
            get_new_user(path)
        else:
            print(f"Welcome back, {username}!")

    else:
        username = get_new_user(path)

        print(f"We'll remember you when you come back, {username}!")

greet_user()
