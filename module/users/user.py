from .baseuser import BaseUser


class User(BaseUser):
    def __init__(self, model):
        super().__init__(model)

    def getTitle(self):
        return f"User with name {self._userName}"

    def getInfo(self):
        return f'Email is {self._email}'
