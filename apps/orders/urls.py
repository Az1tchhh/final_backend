from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.carts.views import ShoppingCartViewSet
from apps.orders.views import OrderViewSet

orders_router = DefaultRouter()
orders_router.register(prefix='', viewset=OrderViewSet, basename='order')


urlpatterns = [
    path('', include(orders_router.urls))
]