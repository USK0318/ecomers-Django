from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return self.product_name

