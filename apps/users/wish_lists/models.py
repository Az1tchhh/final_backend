from django.db import models

from apps.products.models import Product
from apps.utils.models import AbstractModel, TimeStampMixin


# Create your models here.
class WishList(AbstractModel, TimeStampMixin):
    user = models.OneToOneField(to='users.User', on_delete=models.CASCADE)


class WishListItem(AbstractModel, TimeStampMixin):
    wish_list = models.ForeignKey(WishList, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(to='products.Product', on_delete=models.CASCADE)
