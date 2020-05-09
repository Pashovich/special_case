from django.urls import path
from .controllers.makeusercontroller import MakeUserController
from .controllers.startpagecontroller import StartPageController
from .controllers.findusercontroller import FindUserController
from .controllers.usercontroller import UserController

moduleUrls = [
    path('make-user', MakeUserController.as_view(),name='new-user'),
    path('find-user', FindUserController.as_view()),
    path('user/<int:userId>',UserController.as_view(), name='users'),
    path('', StartPageController.as_view())
]
