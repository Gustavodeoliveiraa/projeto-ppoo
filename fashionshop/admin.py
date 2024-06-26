from django.contrib import admin
from fashionshop.models import (
    Product, Categories, ShoppingCart
)


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    fields = (
        'name', 'price', 'image', 'categories'
    )
    search_fields = ('nome', 'categories__nome')
    list_filter = ('categories',)


@admin.register(Categories)
class AdminCategories(admin.ModelAdmin):
    fields = ('name',)
    search_fields = ('nome',)


@admin.register(ShoppingCart)
class AdminShoppingCarts(admin.ModelAdmin):
    fields = ('owner', 'product', 'amount')
