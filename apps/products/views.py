from django.shortcuts import render
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.carts.models import ShoppingCart
from apps.products.models import Product, ProductCategory
from apps.products.serializers import ProductSerializer, ProductCreateSerializer, ProductCategorySerializer, \
    ProductCategoryCreateSerializer, AddToCartSerializer, AddToWishListSerializer, ProductRetrieveSerializer
from apps.products.services import create_new_product, create_product_category, add_product_to_cart
from apps.users.permissions import IsWebUser
from apps.users.wish_lists.models import WishList, WishListItem
from apps.users.wish_lists.services import create_wish_list_item
from apps.utils.serializers import EmptySerializer
from apps.utils.views import BaseViewSet


# Create your views here.
@method_decorator(name='list', decorator=swagger_auto_schema(tags=['product']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['product']))
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['product']))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=['product']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['product']))
class ProductViewSet(BaseViewSet,
                     mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    serializer_class = ProductSerializer
    serializers = {
        'create': ProductCreateSerializer,
        'update': ProductCreateSerializer,
        'retrieve': ProductRetrieveSerializer,
        'destroy': EmptySerializer,
        'add_to_cart': AddToCartSerializer,
        'add_to_wishlist': EmptySerializer
    }
    permission_classes = [IsWebUser]
    queryset = Product.objects.all()

    def perform_create(self, serializer):
        product = create_new_product(serializer.validated_data)
        return product

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        serializer = ProductSerializer(obj, many=False)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['POST'], detail=True, url_path='add-to-cart')
    def add_to_cart(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quantity = serializer.validated_data['quantity']
        user = self.request.user
        product_id = self.kwargs['pk']
        add_product_to_cart(user, product_id, quantity)
        return Response(data={'success': True}, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True, url_path='add-to-wishlist')
    def add_to_wishlist(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        wish_list = WishList.objects.filter(user=self.request.user).first()
        if wish_list is None:
            wish_list = WishList.objects.create(user=self.request.user)

        wish_list_item = create_wish_list_item(wish_list, pk)
        return Response(data={'success': True}, status=status.HTTP_200_OK)


@method_decorator(name='list', decorator=swagger_auto_schema(tags=['product_category']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['product_category']))
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['product_category']))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=['product_category']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['product_category']))
class ProductCategoryViewSet(BaseViewSet,
                             mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             mixins.UpdateModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             GenericViewSet):
    serializer_class = ProductCategorySerializer
    serializers = {
        'create': ProductCategoryCreateSerializer,
        'update': ProductCategoryCreateSerializer,
        'destroy': EmptySerializer
    }
    permission_classes = [IsWebUser]
    queryset = ProductCategory.objects.all()

    def perform_create(self, serializer):
        product_category = create_product_category(serializer.validated_data)
        return product_category

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        serializer = ProductCategorySerializer(obj, many=False)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
