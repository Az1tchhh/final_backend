from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.products.views import ProductViewSet, ProductCategoryViewSet

products_router = DefaultRouter()
products_router.register(prefix='category', viewset=ProductCategoryViewSet, basename='product-category')
products_router.register(prefix='', viewset=ProductViewSet, basename='product')


urlpatterns = [
    path('', include(products_router.urls))
]