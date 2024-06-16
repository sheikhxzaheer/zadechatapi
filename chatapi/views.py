from rest_framework import generics
from .models import *
from .serializers import *
from zadechatapi.utils import zResponse


class ChatView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def list(self, request):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
            return zResponse(status=200, data=data)
        except Exception as e:
            error_message = str(e)
            return zResponse(status=404, data=error_message)
        
    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            serializer
            return zResponse(status=200, message="New Chat Creted")

        except Exception as e:
            return zResponse(status=404, data=str(e))
        

class MessageView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def list(self, request):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
            return zResponse(status=200, data=data)
        except Exception as e:
            error_message = str(e)
            return zResponse(status=404, data=error_message)
        
    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            serializer
            return zResponse(status=200, data=serializer.data)

        except Exception as e:
            return zResponse(status=404, data=str(e))


