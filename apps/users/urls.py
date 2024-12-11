from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.views import CustomTokenObtainPairView, WebUserViewSet, RegistrationViewSet

users_router = DefaultRouter()
users_router.register(prefix='', viewset=WebUserViewSet, basename='user')
users_router.register(prefix='register', viewset=RegistrationViewSet, basename='user-register')

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('wish-lists/', include('apps.users.wish_lists.urls')),
    path('', include(users_router.urls))
]