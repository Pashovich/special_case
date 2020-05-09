from .basecontroller import BaseController
from django.shortcuts import render, redirect
from module.form import Form


class MakeUserController(BaseController):
    __form = Form()

    def get(self, request):
        return render(request, 'form.html', {"form": self.__form})

    def post(self, request):
        self.__form = Form(data = request.data)
        if self.__form.is_valid():
            user = self.__form.save()
            return redirect('users', userId = user.pk)
        else:
            return render(request, 'form.html', {"form": self.__form})
