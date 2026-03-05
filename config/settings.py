from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dev-only-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'config.urls'

INSTALLED_APPS = [
    'channels',
    'chat',
]

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'chat' / 'templates' / 'chat'],
    'APP_DIRS': False,
    'OPTIONS': {'context_processors': ['django.template.context_processors.request']},
}]

ASGI_APPLICATION = 'config.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    }
}