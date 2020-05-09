from .basecontroller import BaseController
from django.shortcuts import render
from module.form import Form
from module.databaseaction.databaseaction import DatabaseActions


class FindUserController(BaseController):
    __usersInfoList = []
    def __init__(self):
        super().__init__()

    def get(self, request):
        return render(request, 'findform.html', {'form': Form()})

    def post(self, request):
        self.__usersInfoList = self._databaseObject.getAllUsersByName(request.data['name'])
        return render(request, 'findform.html', {'form': Form(data = request.data), 'resultList': self.__usersInfoList})
