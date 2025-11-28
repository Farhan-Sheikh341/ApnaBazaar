from django.shortcuts import render
from .models import Product , Category
from django.db.models import Q
# Create your views here.
def product_page(request,slug):
    
    product = Product.objects.get(slug=slug)
    context = {'product':product}
    return render(request,'product/product.html',context)


def all_products(request,category):
    parent = Category.objects.filter(category_name__iexact=category).first()

    if not parent:
        products = Product.objects.none()

    else:
        subcategories = Category.objects.filter(parent=parent)

        products = Product.objects.filter(
            Q(category=parent) | Q(category__in=subcategories)
        )

    context ={
        'products' : products,
        'category' : category
    }
    return render(request,'product/all_products.html',context)
   