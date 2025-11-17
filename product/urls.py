from django.urls import path
from .views import product_page

urlpatterns = [
    path('<slug>/',product_page,name='product_page'),
    # path('products/',all_products,name='all_products'),
]
