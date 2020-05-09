class BaseUser:

    def __init__(self, model):
        self._userName = model.name
        self._email = model.email

    def getTitle(self):
        raise NotImplementedError

    def getInfo(self):
        raise NotImplementedError
