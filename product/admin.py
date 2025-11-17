from django.contrib import admin
from .models import  *

# Register your models here.

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model = productImages

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','category','price',)
    inlines = [ProductImageAdmin]

admin.site.register(Product,ProductAdmin)
admin.site.register(productImages)