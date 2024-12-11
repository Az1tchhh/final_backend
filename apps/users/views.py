from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.permissions import IsWebUser
from apps.users.serializers import CustomTokenObtainPairSerializer, WebUserSerializer, WebUserCreateSerializer
from apps.users.services import create_new_web_user
from apps.utils.serializers import EmptySerializer
from apps.utils.views import BaseViewSet


# Create your views here.
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()


class RegistrationViewSet(BaseViewSet,
                          mixins.CreateModelMixin,
                          GenericViewSet):
    serializer_class = WebUserSerializer
    serializers = {
        'create': WebUserCreateSerializer,
    }

    def perform_create(self, serializer):
        web_user = create_new_web_user(serializer.validated_data)
        return web_user

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        serializer = WebUserSerializer(user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class WebUserViewSet(BaseViewSet,
                     GenericViewSet):
    serializer_class = WebUserSerializer
    serializers = {
        'info': WebUserSerializer,
    }
    permission_classes = [IsWebUser]

    @action(detail=False, methods=['get'], url_path='info')
    def info(self, request):
        serializer = self.get_serializer(request.user.web_user)
        return Response(serializer.data)
