from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from api.models import Product



def get_all(request):
    if request.method=='GET':
        products=Product.objects.all()
        product_json=[model_to_dict(product) for product in products]
        return JsonResponse(product_json,safe=False)
def get_id(request,pk):
        try:
            product=Product.objects.get(id=pk)
        except Product.DoesNotExist as e:
            return JsonResponse({'error':str(e)})
        if request.method=='GET':
            return JsonResponse(model_to_dict(product))

def create(request):
    if request.method=='POST':
        data=json.loads(request.body.decode('utf-8'))

        product=Product.objects.create(
            name=data.get('name'),
            price=data.get('price'),
            quantity=data.get('quantity'),
            description=data.get('description')
            
        )
        return JsonResponse(model_to_dict(product))
def update(request,pk):
        try:
            product=Product.objects.get(id=pk)
        except Product.DoesNotExist as e:
             return JsonResponse ({'error':str(e)})
        if request.method=='PUT':
            data=json.loads(request.body.decode('utf-8'))
            product.name=data.get('name',product.name)
            product.price=data.get('price',product.price)
            product.quantity=data.get('quantity',product.quantity)
            product.description=data.get('description',product.description)

            product.save()

            return JsonResponse(model_to_dict(product))