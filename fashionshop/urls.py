from django.urls import path
from fashionshop.views import Home, cadastra, get_by_name, get_by_categories


urlpatterns = [
    path("", view=Home, name="home"),
    path("register/", view=cadastra, name='cadastra'),
    path("search/", view=get_by_name, name="search"),
    path("categorie/", view=get_by_categories, name="categorie"),
]
