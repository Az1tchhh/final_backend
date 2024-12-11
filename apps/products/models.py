from django.db import models

from apps.utils.models import AbstractModel, TimeStampMixin


# Create your models here.

class ProductCategory(AbstractModel, TimeStampMixin):
    name = models.CharField(max_length=255)
    parent_id = models.IntegerField(null=True)


class Product(AbstractModel, TimeStampMixin):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=False)
