# mychat/settings.py
from pathlib import Path
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'  # Replace with a secure key for production.
DEBUG = True
ALLOWED_HOSTS = []
CELERY_TASK_QUEUES = {
    'email': {'exchange': 'email', 'routing_key': 'email'},
    'long': {'exchange': 'long', 'routing_key': 'long'},
}
CELERY_TASK_ROUTES = {
    'chat.tasks.send_group_email': {'queue': 'email'},
    'chat.tasks.long_task':        {'queue': 'long'},
}
INSTALLED_APPS = [
    # Default Django apps.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps.
    'channels',
    # Local apps.
    'chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mychat.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Global templates folder (if used).
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Needed for auth views.
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mychat.wsgi.application'
ASGI_APPLICATION = 'mychat.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Authentication settings.
LOGIN_REDIRECT_URL = '/chat/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# Channels configuration using Redis.
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
CELERY_BROKER_URL = 'redis://172.18.17.214/0'
CELERY_RESULT_BACKEND = 'redis://172.18.17.214/1'
STATIC_URL = '/static/'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'leo'
EMAIL_HOST_PASSWORD = '11111111'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'no-reply@example.com'
