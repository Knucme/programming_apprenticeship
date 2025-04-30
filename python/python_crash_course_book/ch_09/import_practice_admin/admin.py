from privileges import Privileges
class Users:
    """Creates a user profile"""

    def __init__(self, first_name, last_name, user_name, location):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Descibes the current user"""
        print(f"Name: {self.first_name},{self.last_name}")
        print(f"Bio\n@{self.user_name}\nLocation:{self.location}")
       
    def greet_user(self):
        """Creates a personal greeting to user."""
        print(f"Welcome {self.first_name},{self.last_name}")
    
    def increment_login_attempts(self):
        """Increment login attempt by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0"""
        self.login_attempts = 0



class Admin(Users):
    """Creates a admin user"""

    def __init__(self, first_name, last_name, user_name, location):
        
        super().__init__(first_name, last_name, user_name, location)

        self.privileges = Privileges() 

