from django.db import models
from base.models import BaseModel
from django.utils.text import slugify

# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='categories/')
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories'
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        if self.parent:
            return f"{self.parent.category_name} → {self.category_name}"
        return self.category_name


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    price = models.IntegerField()
    full_price = models.IntegerField(null=True,blank=True)
    product_specification = models.TextField(null=True,blank = True)
    product_description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product,self).save(*args,**kwargs)

    def __str__(self):
            return self.product_name

class productImages(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name = 'product_images')
    image = models.ImageField()
