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

class user_info(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_mobile = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to="profile_pics")

    def __str__(self):
        return self.user_name
class cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    product_id = models.IntegerField()

    def __str__(self):
        return self.user_id

class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.user_id