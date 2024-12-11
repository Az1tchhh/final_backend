from django.db import models

from apps.utils.enums import PaymentMethod, PaymentStatus
from apps.utils.models import AbstractModel, TimeStampMixin


# Create your models here.
class Payment(AbstractModel, TimeStampMixin):
    order = models.OneToOneField(to='orders.Order', on_delete=models.SET_NULL, related_name='payment', null=True)
    payment_method = models.CharField(choices=PaymentMethod.choices, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.CharField(choices=PaymentStatus, default=PaymentStatus.PENDING, null=False)


