from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.reviews.views import ReviewViewSet

review_router = DefaultRouter()
review_router.register(prefix='', viewset=ReviewViewSet, basename='review')


urlpatterns = [
    path('', include(review_router.urls))
]