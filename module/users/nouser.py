from .baseuser import BaseUser


class NoUser(BaseUser):
    def getInfo(self):
        return 'No such user'

    def getTitle(self):
        return ''
