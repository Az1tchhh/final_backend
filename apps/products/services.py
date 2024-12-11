from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from apps.carts.models import ShoppingCart, CartItem
from apps.products.models import Product, ProductCategory


@transaction.atomic
def create_new_product(data):
    product = Product.objects.create(**data)
    return product


def create_product_category(data):
    product_category = ProductCategory.objects.create(**data)
    return product_category


@transaction.atomic
def add_product_to_cart(user, product_id, quantity):
    shopping_cart = ShoppingCart.objects.filter(user=user).first()
    if shopping_cart is None:
        raise ValidationError("You dont have a shopping cart")

    product = get_object_or_404(Product, pk=product_id)

    CartItem.objects.create(shopping_cart=shopping_cart, product=product, quantity=quantity)

    product.stock_quantity -= quantity
    if product.stock_quantity < 0:
        raise ValidationError("We don't have enough stock")
    product.save()
