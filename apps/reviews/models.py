from django.db import models

from apps.utils.models import AbstractModel, TimeStampMixin


# Create your models here.
class Review(AbstractModel, TimeStampMixin):
    product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE, related_name='reviews', null=False)
    user = models.ForeignKey(to='users.User', on_delete=models.SET_NULL, related_name='reviews', null=True)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
