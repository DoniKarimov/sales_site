from django.db import models
from django.contrib.auth.models import AbstractUser
from mptt.models import TreeForeignKey

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='rasm', default='user.png')
    STATUS = (
        ('user', 'user'),
        ('admin', 'Admin')

    )
    status = models.CharField(choices=STATUS, max_length=60, default='user')


class Category(models.Model):
    name = models.CharField(max_length=300)
    parent = TreeForeignKey('self', verbose_name = 'ichki tur', on_delete = models.CASCADE, null=True, blank=True)
    rasm = models.ImageField(upload_to='category.img')

class Product(models.Model):
    name = models.CharField(max_length=100)
    sharx = models.TextField()
    price = models.TextField()
    category = models.ForeignKey(Category,verbose_name = 'category', on_delete=models.CASCADE, related_name='productlar')  
    user = models.ForeignKey(CustomUser,verbose_name='customuser', on_delete=models.CASCADE, related_name='product')
    createtime = models.DateTimeField(auto_now_add=True)  

class Product_img(models.Model):
    rasm = models.ImageField(upload_to='product_img/')
    product = models.ForeignKey(Product,verbose_name='rasm',on_delete=models.CASCADE, related_name='img')  

# class Savat(models.Model):


