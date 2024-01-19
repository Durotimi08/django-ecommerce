from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
def homepage(request):
    products= Product.objects.order_by('-id')
    context = {'products': products}
    return render (request, 'clothings/index.html',context)

def jewellery(request):
    return render (request, 'clothings/jewellery.html')

def electronic(request):
    return render (request, 'clothings/electronic.html')

def fashion(request):
    return render (request, 'clothings/fashion.html')

def base(request):
    return render (request, 'base.html')

def product_upload(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            messages.success(request, "Product upload sucessfully")
            return redirect('homepage')
    else:
        product_form = ProductForm()
    context = {'product_form': product_form}
    return render(request, 'clothings/product_upload.html', context)
