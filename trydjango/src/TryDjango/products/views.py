from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import HttpResponse

from .models import Product
from .forms import ProductForm, RawProductionForm

# Create your views here.

def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id = 1)
    """context = {
        "title":obj.title,
        "description":obj.description,
        "featured":obj.featured,
    }"""

    context = {}
    return render (request, "products/product_detail.html", context)  


"""def create_view(request, *args, **kwargs):
    my_form = RawProductionForm()
    if request.method == "POST":
        my_form = RawProductionForm(request.POST)

        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)

        else:
            print(my_form.errors)    

    context = {
        "form":my_form
    }
    return render (request, "products/product_create.html", context)"""



def create_view(request, *args, **kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    
    
    #obj = Product.objects.get(id = 1)
    
    
    context = {
        'form':form
    }
    return render (request, "products/product_create.html", context)


"""def create_view(request, *args, **kwargs):
    #print(request.GET)
    #print(request.POST)

    my_new_title = request.POST.get('title')
    print(my_new_title)
    #Product.objects.create(title=my_new_title)
    context = {}
    return render (request, "products/product_create.html", context)"""


def render_initial_data(request):
    initial_data = {
        'title': "My this awesome title"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)



"""def dynamic_lookup_view(request, id):
    try:
        obj = get_object_or_404(Product, id=id)
    except Product.DoesNotExist:
        raise "Http404"
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)"""



def dynamic_lookup_view(request, id):
    #obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    # obj = Product.objects.get(id=id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)



def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    #POST request
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)


