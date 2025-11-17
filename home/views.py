from django.shortcuts import render
from product.models import Product
# Create your views here.

def home_page(request):
    electronics = Product.objects.filter(category__parent__category_name='electronics')
    fashions = Product.objects.filter(category__parent__category_name='fashions')
    jewellery = Product.objects.filter(category__category_name='jewellery')
    beauty_and_personal_care = Product.objects.filter(category__category_name = 'beauty_and_personal_care')
    winter_wear = Product.objects.filter(category__category_name='winter_wear')
    home_kitchen_and_decor = Product.objects.filter(category__category_name='home_kitchen_and_decor')
    context = {'electronics':electronics,
               'fashions':fashions,
               'jewellery': jewellery,
               'beauty_and_personal_care': beauty_and_personal_care,
               'winter_wear':winter_wear,
               'home_kitchen_and_decor':home_kitchen_and_decor,
               
               }
    return render(request,'home/home.html',context)

