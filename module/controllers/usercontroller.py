from rest_framework.views import APIView
from django.shortcuts import render
from ..databaseaction.databaseaction import DatabaseActions
from ..models import ModelData


class UserController(APIView):

    def get(self, request, userId):
        action = DatabaseActions()
        model = action.getUserInfoById(userId = userId)
        print('model',model)
        return render(request, 'userform.html', {'model': model})
