class Privileges:
    def __init__(self):
        self.privileges =  [
                "can add post", "can delete post", "can ban user"
                ]
    def show_privileges(self):
        """Shows what privileges the admin has."""
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


