from django.shortcuts import render
from .models import Product
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def Home(request):
    products = Product.objects.all()

    return render(
        request, template_name="home.html", context={'products': products}
    )


def get_by_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        products = Product.objects.filter(name__icontains=name)

    return render(
        request, template_name="home.html", 
        context={'products': products}
    )


def get_by_categories(request):
    if request.method == 'POST':
        categorie = request.POST.get('categories')
        products = Product.objects.filter(categories__name__icontains=categorie)

    return render(
        request, template_name="home.html", 
        context={'products': products}
    )


def cadastra(request):
    return render(request, template_name="partials/register.html")
