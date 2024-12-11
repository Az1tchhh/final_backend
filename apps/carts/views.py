from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.carts.models import ShoppingCart
from apps.carts.serializers import ShoppingCartSerializer
from apps.users.permissions import IsWebUser
from apps.utils.serializers import EmptySerializer
from apps.utils.views import BaseViewSet


# Create your views here.
class ShoppingCartViewSet(BaseViewSet,
                          mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.DestroyModelMixin,
                          GenericViewSet):
    serializer_class = ShoppingCartSerializer
    serializers = {
        'create': EmptySerializer,
        'destroy': EmptySerializer
    }
    permission_classes = [IsWebUser]
    queryset = ShoppingCart.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        shopping_cart = ShoppingCart.objects.create(user=user)
        return shopping_cart

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        serializer = ShoppingCartSerializer(obj, many=False)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['GET'], detail=False, url_path='my')
    def my(self, request, *args, **kwargs):
        user = self.request.user
        shopping_cart = ShoppingCart.objects.filter(user=user).first()
        if shopping_cart is None:
            raise ValidationError("You dont have a shopping cart")

        serializer = self.get_serializer(shopping_cart)
        return Response(data=serializer.data, status=status.HTTP_200_OK)