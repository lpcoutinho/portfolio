"""
Configurações de desenvolvimento.
"""

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ngq8#n&8hvgaue)0z0nl=u3**lm4t1q%vjfeon279(v5ni#nr('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Development-specific apps
# INSTALLED_APPS += [
#     'django_extensions',  # Para shell_plus e outras ferramentas úteis
# ]