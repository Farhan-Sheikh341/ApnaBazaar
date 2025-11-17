from django.shortcuts import render
from .models import Product
# Create your views here.
def product_page(request,slug):
    
    product = Product.objects.get(slug=slug)
    context = {'product':product}
    return render(request,'product/product.html',context)


# def all_products(request):
#     products = Product.objects.all()
#     context ={
#         'products' : products
#     }
#     return render(request,'product/all_products.html',context)
   