from rest_framework import serializers

from apps.products.models import Product, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = (
            'id',
            'name',
            'parent_id',
        )


class ProductCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = (
            'name',
            'parent_id',
        )


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'stock_quantity',
            'category',
        )


class ProductCreateSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.values_list('id', flat=True), required=True)

    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'price',
            'stock_quantity',
            'category_id',
        )


class AddToCartSerializer(serializers.Serializer):
    quantity = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
