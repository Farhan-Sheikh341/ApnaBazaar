from django.urls import path
from .views import product_page,all_products

urlpatterns = [
    path('<str:category>',all_products,name='all_products'),
    path('<slug>/',product_page,name='product_page'),
]
