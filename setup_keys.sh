docker run digitalshoestring/shoestring-django:v0.0.1 python -c "from django.core.management.utils import get_random_secret_key; print(f'SECRET_KEY={get_random_secret_key()}')" > django_secret_key
