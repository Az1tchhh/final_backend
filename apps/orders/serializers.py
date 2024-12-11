from rest_framework import serializers

from apps.orders.models import Order, OrderItem


class OrderItemsSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='product.id')
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2)

    class Meta:
        model = OrderItem
        fields = (
            'id',
            'order_id',
            'product_id',
            'product_name',
            'product_price',
            'quantity',
        )


class OrderSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username')
    items = OrderItemsSerializer(many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = (
            'id',
            'user_id',
            'username',
            'items',
            'total_price',
        )

    def get_total_price(self, obj):
        items = obj.items.all()
        total_price = 0
        for item in items:
            total_price += item.product.price * item.quantity

        return total_price


class OrderCreateSerializer(serializers.Serializer):
    cart_id = serializers.IntegerField(required=True)
