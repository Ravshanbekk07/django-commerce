from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from .models import Product



def get_all(request):
    if request.method=='GET':
        products=Product.objects.all()
        product_json=[model_to_dict(product) for product in products]
        return JsonResponse(product_json,safe=False)