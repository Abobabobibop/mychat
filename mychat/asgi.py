# mychat/asgi.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mychat.settings")
django.setup()  # Примусове налаштування Django

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(chat.routing.websocket_urlpatterns)
    ),
})
