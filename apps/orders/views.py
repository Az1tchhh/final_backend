from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer, OrderCreateSerializer
from apps.orders.services import create_new_order
from apps.users.permissions import IsWebUser
from apps.utils.enums import OrderStatus
from apps.utils.serializers import EmptySerializer
from apps.utils.views import BaseViewSet


# Create your views here.
class OrderViewSet(BaseViewSet,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    serializer_class = OrderSerializer
    serializers = {
        'create': OrderCreateSerializer,
        'destroy': EmptySerializer
    }
    permission_classes = [IsWebUser]
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        order = create_new_order(self.request.user, serializer.validated_data)
        return order

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        serializer = OrderSerializer(obj, many=False)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['GET'], detail=False, url_path='my')
    def my(self, request, *args, **kwargs):
        user = self.request.user
        orders = Order.objects.filter(user=user).prefetch_related(
            'items',
            'status_history'
        )

        serializer = self.get_serializer(orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)