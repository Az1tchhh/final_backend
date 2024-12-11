from django.db import models


class AbstractModel(models.Model):

    objects = models.Manager()

    class Meta:
        abstract = True


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True, null=True)

    class Meta:
        abstract = True
