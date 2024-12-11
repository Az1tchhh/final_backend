from celery import shared_task

from apps.products.models import Product


@shared_task()
def recalculate_review_rating(product_id):
    product = Product.objects.get(pk=product_id)
    reviews = product.reviews.all()
    total_review_rating = 0
    for review in reviews:
        total_review_rating += review.rating
    print(total_review_rating)
    print(reviews.count())
    avg_rating = total_review_rating / reviews.count()
    print(avg_rating)
    product.avg_rating = avg_rating
    product.save()
