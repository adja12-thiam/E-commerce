from django.http import JsonResponse
from .models import Product

def get_products(request):
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)
