from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
# Create your views here.

#importamos el modelo que creamos en el archivo models.py de de la app
from .forms import ProductForm, RawProductForm

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def render_initial_data(request):
    initial_data = {
        'title': "Este es mi titulo"
    }  
    form = RawProductForm(request.POST or None, initial=initial_data)
    if (form.is_valid()):
        print(form.cleaned_data)
        Product.objects.create(**form.cleaned_data)
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def dynamic_lookup_view(request, id):
   # obj = Product.objects.get(id=my_id)
   # obj = get_object_or_404(Product, id=my_id)
    try:
       obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404   
    context = {
        "object": obj
    }
    
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if(request.method == "POST"):
        #confirming delete
        obj.delete()
        return redirect('../../list/')
    #obj.delete()
    context = {
        "object": obj,
        "id": id
    }
    return render(request, "products/product_delete.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=1)
    #context = {
    #    'title': obj.title,
    #    'description': obj.description
    #}
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
    form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

# def product_create_view(request):
#     #print (request.GET)
#     #print (request.POST['title'])
#     # if request.method == "POST":
#     #     my_title = request.POST.get('title')
#     #     print(my_title)
#     #     #Product.objects.create(title=my_title)
#     #context = {}
#     my_form = RawProductForm() #by default
#     if request.method == "POST": 
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             #now the data is good
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             #errors
#             print(my_form.errors)
#     context = {
#         "form": my_form,
#     }
#     return render(request, "products/product_create.html", context)

