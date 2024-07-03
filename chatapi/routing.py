from django.urls import path
from .consumers import ChatConsumer


websocket_urlpatterns = [
    # path(r'asyncChat', ChatConsumer.as_asgi()),
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
]