from rest_framework import serializers

from apps.orders.models import Order
from apps.payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = (
            'id',
            'order_id',
            'payment_method',
            'amount',
            'status',
            'created_at',
            'updated_at',
        )


class PaymentCreateSerializer(serializers.ModelSerializer):
    order_id = serializers.PrimaryKeyRelatedField(queryset=Order.objects.values_list('id', flat=True), required=True)

    class Meta:
        model = Payment
        fields = (
            'order_id',
            'payment_method',
        )
