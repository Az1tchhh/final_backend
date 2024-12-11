from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.carts.views import ShoppingCartViewSet

carts_router = DefaultRouter()
carts_router.register(prefix='', viewset=ShoppingCartViewSet, basename='shopping_cart')


urlpatterns = [
    path('', include(carts_router.urls))
]