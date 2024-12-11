from django.db import transaction
from rest_framework.exceptions import ValidationError

from apps.users.models import User, WebUser


@transaction.atomic
def create_new_web_user(data):
    username = data.pop('username')
    password = data.pop('password')

    existing_user = User.objects.filter(username=username).first()
    if existing_user:
        raise ValidationError("Choose another username")

    email = data.get('email')
    existing_web_user = WebUser.objects.filter(email=email).first()
    if existing_web_user:
        raise ValidationError("Choose another email")

    user = User.objects.create_user(username, password)

    web_user = WebUser.objects.create(**data, user=user)
    return web_user
