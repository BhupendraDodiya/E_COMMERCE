from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register((Product))
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','selling_price','discounted_price','description','brand','category','product_image']
