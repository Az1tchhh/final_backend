from rest_framework import serializers

from apps.reviews.models import Review
from apps.users.serializers import WebUserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = WebUserSerializer(source='user.web_user')

    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'rating',
            'comment',
            'created_at',
            'updated_at'
        )


class ReviewCreateSerializer(serializers.ModelSerializer):
    from apps.products.models import Product
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.values_list('id', flat=True), required=True)

    class Meta:
        model = Review
        fields = (
            'product_id',
            'rating',
            'comment',
        )

