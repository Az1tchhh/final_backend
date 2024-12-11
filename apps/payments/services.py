from django.db import transaction
from django.db.models import Sum, F
from rest_framework.generics import get_object_or_404

from apps.orders.models import Order, OrderItem
from apps.payments.models import Payment


@transaction.atomic
def create_payment(data):
    order_id = data.pop('order_id')

    order = get_object_or_404(Order, id=order_id)

    items = OrderItem.objects.filter(order_id=order_id).select_related(
        'product',
    )

    total_amount = items.annotate(
        item_total=F('product__price') * F('quantity')
    ).aggregate(
        total=Sum('item_total')
    )['total']

    data['amount'] = total_amount

    payment = Payment.objects.create(order=order, **data)

    return payment
