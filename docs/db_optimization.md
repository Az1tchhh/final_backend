# Database Optimization Strategies

## 1. Indexing
- **Primary Keys**: Automatically indexed.
- **Foreign Keys**: Add indexes to speed up JOIN operations.
  

#### I created indexes on datetime fields, such as created_at and updated_at. The chance of having two same datetime fields in a table is miscible, and it will be much faster when we will process filtering by dates, therefore it will be the best practice to index datetime field.


```python
payments/services.py
items = OrderItem.objects.filter(order_id=order_id).select_related(
        'product',
    )
   
orders/views.py
orders = Order.objects.filter(user=user).prefetch_related(
            'items'
        )

    