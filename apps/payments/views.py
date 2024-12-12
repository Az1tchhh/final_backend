from django.shortcuts import render
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.payments.models import Payment
from apps.payments.serializers import PaymentSerializer, PaymentCreateSerializer
from apps.payments.services import create_payment
from apps.users.permissions import IsWebUser
from apps.utils.serializers import EmptySerializer
from apps.utils.views import BaseViewSet


# Create your views here.
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['payment']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['payment']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['payment']))
class PaymentViewSet(BaseViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    serializer_class = PaymentSerializer
    serializers = {
        'create': PaymentCreateSerializer,
        'destroy': EmptySerializer,
    }
    permission_classes = [IsWebUser]
    queryset = Payment.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_superuser:
            return queryset

        queryset = queryset.filter(order__user=user)
        return queryset

    def perform_create(self, serializer):
        payment = create_payment(serializer.validated_data)
        return payment

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        serializer = PaymentSerializer(obj, many=False)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)