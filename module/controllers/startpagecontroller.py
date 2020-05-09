from .basecontroller import BaseController
from django.shortcuts import render


class StartPageController(BaseController):
    def get(self, request):
        return render(request, 'chooseform.html')
