from django.urls import path
from fashionshop.views import (
    Home, cadastra, get_by_name, get_by_categories, shoppingcart, add_to_cart,
    remove_from_cart
)


urlpatterns = [
    path("", view=Home, name="home"),
    path("register/", view=cadastra, name='cadastra'),
    path("search/", view=get_by_name, name="search"),
    path("categorie/", view=get_by_categories, name="categorie"),
    path("cart/", view=shoppingcart, name="cart"),
    path("cart/add/<int:product_id>", view=add_to_cart, name="add"),
    path('cart/remove/<int:item_id>/', view=remove_from_cart, name='remove'),
]
