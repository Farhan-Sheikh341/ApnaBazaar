from django.shortcuts import render
from .models import Product
# Create your views here.
def product_page(request,slug):
    
    product = Product.objects.get(slug=slug)
    context = {'product':product}
    return render(request,'product/product.html',context)


def all_products(request,category):
    products = Product.objects.filter(category__category_name__iexact=category)
    context ={
        'products' : products,
        'category' : category
    }
    return render(request,'product/all_products.html',context)
   