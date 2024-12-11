from django.db import models

from apps.utils.models import AbstractModel, TimeStampMixin


# Create your models here.
class ShoppingCart(AbstractModel, TimeStampMixin):
    user = models.OneToOneField(to='users.User', on_delete=models.CASCADE, related_name='shopping_cart')


class CartItem(AbstractModel, TimeStampMixin):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.PROTECT, related_name='cart_items')
    product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1)
