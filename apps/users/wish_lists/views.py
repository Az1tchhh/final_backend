from django.shortcuts import render
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from apps.users.permissions import IsWebUser
from apps.users.wish_lists.models import WishList
from apps.users.wish_lists.serializers import WishListSerializer
from apps.utils.serializers import EmptySerializer
from apps.utils.views import BaseViewSet


# Create your views here.
@method_decorator(name='list', decorator=swagger_auto_schema(tags=['wish-list']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['wish-list']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['wish-list']))
class WishListViewSet(BaseViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    serializer_class = WishListSerializer
    serializers = {
        'destroy': EmptySerializer,
    }
    permission_classes = [IsWebUser]
    queryset = WishList.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_superuser:
            return queryset

        queryset = queryset.filter(user=user)
        return queryset
