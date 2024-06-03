from django.shortcuts import render, redirect
from .models import Product, FormRegister
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


@csrf_exempt
def Home(request):
    products = Product.objects.all().order_by('-id')

    return render(
        request, template_name="home.html", context={'products': products}
    )


def get_by_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        products = Product.objects.filter(name__icontains=name).order_by('-id')

        message = False

        if not products.exists():
            message = "Nenhum produto encontrado"

    return render(
        request, template_name="home.html",
        context={'products': products, 'message': message}
    )


def get_by_categories(request):
    if request.method == 'POST':
        categorie = request.POST.get('categories')
        products = Product.objects.filter(
            categories__name__icontains=categorie
        ).order_by('-id')

    return render(
        request, template_name="home.html", 
        context={'products': products}
    )


@csrf_exempt
def cadastra(request):
    if request.method == 'GET':
        form = FormRegister()

    if request.method == 'POST':
        form = FormRegister(request.POST)

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(email=email).exists():
            User.objects.create(
                username=username, email=email, password=password
            )

            messages.success(request, 'Cadastrado com sucesso')

            return redirect('home')

    return render(
        request, template_name="partials/register.html", context={'form': form}
    )
