"""
Configurações de produção.
"""

from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-me-in-production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'lpcoutinho.top', 
    'www.lpcoutinho.top',
    'localhost',
    '127.0.0.1',
]

# CSRF Configuration
CSRF_TRUSTED_ORIGINS = [
    'https://lpcoutinho.top',
    'https://www.lpcoutinho.top',
    'http://lpcoutinho.top',
    'http://www.lpcoutinho.top',
]

# Database - SQLite em diretório persistente
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/app/data/db.sqlite3',
        'OPTIONS': {
            'timeout': 60,
        }
    }
}

# WhiteNoise para servir arquivos estáticos
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Security settings (relaxadas para HTTP inicial)
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Session and CSRF Security (HTTPS habilitado via Let's Encrypt)
SESSION_COOKIE_SECURE = True  # Habilitado para HTTPS
CSRF_COOKIE_SECURE = True     # Habilitado para HTTPS
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True   # Habilitado para segurança
SESSION_COOKIE_SAMESITE = 'Strict'
CSRF_COOKIE_SAMESITE = 'Strict'

# HSTS Settings
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Static files for production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configurações de logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

# Debug temporário para CSRF (remover depois)
def csrf_failure_debug(request, reason=""):
    from django.http import HttpResponse
    return HttpResponse(f"CSRF failure: {reason}")

CSRF_FAILURE_VIEW = csrf_failure_debug