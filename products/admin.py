from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product

# Регистрируем модель Категории
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Что показывать в списке
    search_fields = ('name',)  # По каким полям можно искать

# Регистрируем модель Товара
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_available', 'created_at')
    list_filter = ('category', 'is_available', 'created_at')  # Фильтры справа
    search_fields = ('name', 'description')
    list_editable = ('price', 'is_available')  # Можно редактировать прямо в списке