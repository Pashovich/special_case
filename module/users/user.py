from .baseuser import BaseUser
class User(BaseUser):
    def __init__(self, model):
        self.userName = model.name
        self.email = model.email

    def getTitle(self):
        return f"User with name {self.userName}"

    def getInfo(self):
        return f'Email is {self.email}'
