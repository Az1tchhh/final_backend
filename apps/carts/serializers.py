from rest_framework import serializers

from apps.carts.models import CartItem, ShoppingCart


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2)

    class Meta:
        model = CartItem
        fields = (
            'id',
            'product_id',
            'product_name',
            'product_price',
            'quantity',
        )


class ShoppingCartSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username')
    cart_items = CartItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingCart
        fields = (
            'id',
            'user_id',
            'username',
            'cart_items',
            'total_price',
        )

    def get_total_price(self, obj):
        cart_items = obj.cart_items.all()
        total_price = 0
        for cart_item in cart_items:
            total_price += cart_item.product.price * cart_item.quantity

        return total_price
