from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

from apps.products.models import Product
from apps.users.wish_lists.models import WishListItem


def create_wish_list_item(wish_list, product_id):
    product = get_object_or_404(Product, id=product_id)
    existing_wish_list_items = wish_list.items.filter(product_id=product.id).exists()
    if existing_wish_list_items:
        raise ValidationError("This product is in wish list already")

    wish_list_item = WishListItem.objects.create(wish_list=wish_list, product=product)

    return wish_list_item
