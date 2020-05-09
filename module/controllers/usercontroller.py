from rest_framework.views import APIView
from django.shortcuts import render
from ..databaseaction.databaseaction import DatabaseActions


class UserController(APIView):
    def get(self, request, userId):
        action = DatabaseActions()
        user = action.getUserById(userId = userId)
        model = {}
        model['title'] = user.getTitle()
        model['info'] = user.getInfo()
        return render(request, 'userform.html', {'model': model})
