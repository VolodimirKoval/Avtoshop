from django.contrib import admin

# Register your models here.
from market.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class Admin(admin.ModelAdmin):
    pass
