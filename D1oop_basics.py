# Class = Blueprint
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display(self):
        print(f"User: {self.username}, Email: {self.email}")


# Inheritance
class Admin(User):
    def __init__(self, username, email, role):
        super().__init__(username, email)
        self.role = role

    def display(self):
        print(f"Admin: {self.username}, Role: {self.role}")


# Polymorphism in action
def show_user(user):
    user.display()


# Main program
u1 = User("john_doe", "john@example.com")
a1 = Admin("super_admin", "admin@example.com", "Moderator")

show_user(u1)  # User
show_user(a1)  # Admin
