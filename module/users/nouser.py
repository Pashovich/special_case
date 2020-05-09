from .baseuser import BaseUser


class NoUser(BaseUser):
    def __init__(self):
        pass

    def getInfo(self):
        return 'No such user'

    def getTitle(self):
        return ''
