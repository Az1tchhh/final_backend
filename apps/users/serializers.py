from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.models import User, WebUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        if hasattr(self.user, 'web_user'):
            data['email'] = self.user.web_user.email
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class WebUserSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = WebUser
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        )

    def get_username(self, obj):
        return obj.user.username


class WebUserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
