from django.db.models import TextChoices


class OrderStatus(TextChoices):
    PAID = 'paid', 'paid',
    WAITING_FOR_PAYMENT = 'waiting_for_payment', 'waiting_for_payment',
    GIVEN_TO_DELIVERY_SERVICE = 'given_to_delivery_service', 'given_to_delivery_service',
    READY_TO_PICKUP = 'ready_to_pickup', 'ready_to_pickup',
    GIVEN = 'given', 'given'


class PaymentMethod(TextChoices):
    CARD = 'card', 'card',
    CASH = 'cash', 'cash'


class PaymentStatus(TextChoices):
    PENDING = 'pending', 'pending',
    SUCCESS = 'success', 'success',
    FAILURE = 'failure', 'failure',