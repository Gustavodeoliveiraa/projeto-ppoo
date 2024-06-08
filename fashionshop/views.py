from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, FormRegister, ShoppingCart, CartItem
from django.contrib.auth.decorators import login_required
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


def shoppingcart(request):
    cart, created = ShoppingCart.objects.get_or_create(owner=request.user)

    return render(
        request, template_name="partials/shoppingcart.html",
        context={'cart': cart, 'total': cart.total() if not created else 0}
    )


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = ShoppingCart.objects.get_or_create(owner=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.info(request, 'Item adicionado ao carrinho')

    return redirect('home')


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__owner=request.user)
    cart_item.delete()

    return redirect('cart')
