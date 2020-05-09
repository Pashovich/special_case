from ..models import ModelData
from module.users.user import User
from module.users.nouser import NoUser


class DatabaseActions:
    def __getInfo(self, user):
        model = dict()
        model['title'] = user.getTitle()
        model['info'] = user.getInfo()
        return model

    def getUserInfoById(self, userId):
        try:
            model = ModelData.objects.get(pk = userId)
            user = User(model)
            return self.__getInfo(user)
        except:
            user = NoUser()
            return self.__getInfo(user)

    def getAllUsersByName(self, name):
        userList = ModelData.objects.all().filter(name = name)
        if len(userList) != 0:
            return [User(model).getInfo() for model in userList]
        else:
            return [NoUser().getInfo()]
