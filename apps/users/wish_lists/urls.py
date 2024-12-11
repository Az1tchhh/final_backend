from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.products.views import ProductViewSet, ProductCategoryViewSet
from apps.users.wish_lists.views import WishListViewSet

wish_list_router = DefaultRouter()
wish_list_router.register(prefix='', viewset=WishListViewSet, basename='wish-list')


urlpatterns = [
    path('', include(wish_list_router.urls))
]