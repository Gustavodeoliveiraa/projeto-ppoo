from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class Categories(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images', blank=False, null=False)
    categories = models.ForeignKey(
        to=Categories, on_delete=models.PROTECT, blank=False, null=False,
    )

    def __str__(self) -> str:
        return self.name


class ShoppingCarts(models.Model):
    owner = models.ForeignKey(
        to=User, on_delete=models.PROTECT, blank=False, null=False
    )
    product = models.ForeignKey(
        to=Product, on_delete=models.PROTECT, blank=False, null=False
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.owner.username}'


class FormRegister(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Seu nome'}
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'exemplo@gmail.com'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Senha'}
        )
    )

    confirm_password = forms.CharField(
        label='Confirmar senha',
        max_length=255,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirmar senha'}
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):

        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')

        if password1 != password2:
            self.add_error('confirm_password', 'As senhas são diferentes.')

            return self.cleaned_data
        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'Este email já está em uso.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'Este nome já está em uso.')
        return username
