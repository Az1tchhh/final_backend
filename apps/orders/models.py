from django.db import models

from apps.utils.enums import OrderStatus
from apps.utils.models import AbstractModel, TimeStampMixin


# Create your models here.
class Order(AbstractModel, TimeStampMixin):
    user = models.ForeignKey(to='users.User', on_delete=models.PROTECT, related_name='orders', null=False)
    status = models.CharField(choices=OrderStatus.choices)


class OrderItem(AbstractModel, TimeStampMixin):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items', null=False)
    product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)


class OrderStatusHistory(AbstractModel, TimeStampMixin):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='status_history')

    def __str__(self):
        return f"{self.order.id} - {self.order.status} ({self.updated_at})"

