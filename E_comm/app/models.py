from django.db import models
from django.contrib.auth.models import User

# Create your models here.
product_choice = (
    ('mobile','mobile'),
    ('laptop','laptop'),
    ('top wear','top wear'),
    ('bottom wear','bottom wear'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices= product_choice,max_length=100)
    product_image = models.ImageField(upload_to='product/')

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default =1)
    