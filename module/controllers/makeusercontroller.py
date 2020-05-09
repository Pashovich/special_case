from .basecontroller import BaseController
from django.shortcuts import render, redirect
from module.form import Form


class MakeUserController(BaseController):
    def get(self, request):
        form = Form()
        return render(request, 'form.html', {"form": form})

    def post(self, request):
        form = Form(data = request.data)
        if form.is_valid():
            user = form.save()
            return redirect('users', userId = user.pk)
        else:
            return render(request, 'form.html', {"form": form})
