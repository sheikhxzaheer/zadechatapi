from django.urls import path
from .consumers import ChatConsumer


websocket_urlpatterns = [
    path(r'asyncChat', ChatConsumer.as_asgi()),
]