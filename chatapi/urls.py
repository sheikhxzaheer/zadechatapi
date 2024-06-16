from django.urls import path
from .views import *


urlpatterns = [
    path("chat/", ChatView.as_view()),
    path("message/", MessageView.as_view()),
     path("chat/<int:pk>/", ChatDetails.as_view()),
]