from rest_framework import serializers

from apps.products.serializers import ProductSerializer
from apps.users.wish_lists.models import WishList, WishListItem


class WishListItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = WishListItem
        fields = (
            'id',
            'product'
        )


class WishListSerializer(serializers.ModelSerializer):
    items = WishListItemSerializer(many=True)

    class Meta:
        model = WishList
        fields = (
            'id',
            'items',
        )
