# models.py
class User:
    def __init__(self, name, email, mobile):
        self.name = name.lower()
        self.email = email
        self.mobile = mobile