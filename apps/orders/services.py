from django.db import transaction
from rest_framework.generics import get_object_or_404

from apps.carts.models import ShoppingCart, CartItem
from apps.orders.models import Order, OrderItem
from apps.utils.enums import OrderStatus

@transaction.atomic
def create_new_order(user, data):
    cart_id = data.pop('cart_id')
    shopping_cart = get_object_or_404(ShoppingCart, id=cart_id)
    order = Order.objects.create(user=user, status=OrderStatus.WAITING_FOR_PAYMENT)
    shopping_cart_items = shopping_cart.cart_items.all()
    for cart_item in shopping_cart_items:
        order_item = OrderItem.objects.create(order=order, product=cart_item.product)
        order_item.quantity = cart_item.quantity
        order_item.save()
    shopping_cart_items.delete()
    return order