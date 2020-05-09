from .basecontroller import BaseController
from django.shortcuts import render
from module.form import Form
from module.databaseaction.databaseaction import DatabaseActions


class FindUserController(BaseController):
    def get(self, request):
        return render(request, 'findform.html', {'form': Form(), 'answer': ''})

    def post(self, request):
        users = DatabaseActions().getAllUsersByName(request.data['name'])
        userList = [item.getInfo() for item in users]
        return render(request, 'findform.html', {'form': Form(data = request.data), 'resultList': userList})
