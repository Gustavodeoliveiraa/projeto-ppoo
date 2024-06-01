from django.db import models
from django.contrib.auth.models import User


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
