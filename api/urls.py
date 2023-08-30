from django.urls import path

from .views import get_all,create,get_id

urlpatterns=[
    path('',get_all),
    path('create',create),
    path('<int:pk>',get_id),
]


