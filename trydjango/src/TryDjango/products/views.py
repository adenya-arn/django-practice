from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Product
# Create your views here.

def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id = 1)
    context = {
        "title":obj.title,
        "description":obj.description,
        "featured":obj.featured,
    }
    return render (request, "Product/detail.html", context)  
