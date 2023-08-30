from django.urls import path
from .views import get_all
 


urlpatterns = [
    path('products/all',get_all)
]