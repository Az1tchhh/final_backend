# Database Optimization Strategies

## 1. Indexing
- **Primary Keys**: Redis as a message broker.
- **Foreign Keys**: Celery.
  

#### Celery used for async tasks (e.g reviews/tasks.py), redis as a memory database. Redis will store tasks queue whenever the server is turned off or on, therefore providing consistency.

