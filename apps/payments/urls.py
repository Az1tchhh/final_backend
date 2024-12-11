from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.payments.views import PaymentViewSet

payment_router = DefaultRouter()
payment_router.register(prefix='', viewset=PaymentViewSet, basename='review')


urlpatterns = [
    path('', include(payment_router.urls))
]