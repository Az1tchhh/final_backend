from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerializer, ReviewCreateSerializer
from apps.reviews.services import delete_review, create_review
from apps.users.permissions import IsWebUser
from apps.users.wish_lists.models import WishList
from apps.users.wish_lists.serializers import WishListSerializer
from apps.utils.serializers import EmptySerializer
from apps.utils.views import BaseViewSet


# Create your views here.
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['review']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['review']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['review']))
class ReviewViewSet(BaseViewSet,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    serializer_class = ReviewSerializer
    serializers = {
        'create': ReviewCreateSerializer,
        'destroy': EmptySerializer,
    }
    permission_classes = [IsWebUser]
    queryset = Review.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = self.perform_create(serializer)
        serializer = ReviewSerializer(obj, many=False)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        data = serializer.validated_data
        user = self.request.user
        review = create_review(data, user)
        return review

    def perform_destroy(self, instance):
        delete_review(instance)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
