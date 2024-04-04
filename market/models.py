# Create your models here.
from django.db import models
import os
from users.models import User


# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, blank=False, null=False, unique=True)
    description = models.CharField(max_length=128, blank=False, null=False)
    image = models.ImageField(upload_to=f'category/images')

    def __str__(self):
        return f"{self.name} | {self.description}"


# Функція, шо додає шлях до збереження зображення продукту згідно категорії продукту
def auto_image_folder(instance, filename):
    category_name = instance.category.name
    return os.path.join(f'goods/images/{category_name}', filename)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    site_name = models.CharField(max_length=50, blank=True, null=True, unique=True)
    name = models.CharField(max_length=128, blank=False, null=False, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to=auto_image_folder)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.product_sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f"Товари для: {self.user.username} | Продукт: {self.product.name}"

    def product_sum(self):
        return self.product.price * self.quantity
