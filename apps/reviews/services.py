from apps.products.models import Product
from apps.reviews.models import Review
from apps.reviews.tasks import recalculate_review_rating

def delete_review(review):
    product = review.product
    review.delete()
    recalculate_review_rating.apply_async(args=[product.id])


def create_review(data, user):
    product_id = data.pop('product_id')

    product = Product.objects.get(pk=product_id)

    review = Review.objects.create(
        user=user,
        product=product,
        **data
    )
    recalculate_review_rating.apply_async(args=[product.id])

    return review
