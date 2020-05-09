from ..models import FormModel
from module.users.user import User
from module.users.nouser import NoUser


class DatabaseActions:

    def getUserById(self, userId):
        try:
            model = FormModel.objects.get(pk = userId)
            return User(model)
        except:
            return NoUser()

    def getAllUsersByName(self, name):
        userList = FormModel.objects.all().filter(name = name)
        if len(userList) != 0:
            return [User(model) for model in userList]
        else:
            return [NoUser()]
