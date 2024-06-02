from django.contrib import admin
from .models import Person, Car, Product, Order, OrderPosition

# Register your models here.

class OrderPositionInLine(admin.TabularInline):
    model = OrderPosition
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'units', 'price', 'category']
    list_filter = ['category']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address']
    inlines = [OrderPositionInLine,]

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'color']
    list_filter = ['brand', 'model']

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car']
    list_filter = ['name']


    pass
