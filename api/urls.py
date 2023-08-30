from django.urls import path

from .views import get_all,create

urlpatterns=[
    path('',get_all),
    path('create/',create),
]


