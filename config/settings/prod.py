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

# Session and CSRF Security (adaptado para HTTP/HTTPS misto)
SESSION_COOKIE_SECURE = False  # Manter False enquanto não tiver HTTPS completo
CSRF_COOKIE_SECURE = False     # Manter False enquanto não tiver HTTPS completo
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False   # Precisa ser False para funcionar com JavaScript
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'

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