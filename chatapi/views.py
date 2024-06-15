from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *


class ChatView(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def list(self, request):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
            return Response(status=200, data=data)
        except Exception as e:
            error_message = str(e)
            return Response(status=404, data=error_message)
        
    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            serializer
            return Response(status=200 , data=serializer.data)

        except Exception as e:
            return Response(status=404, data=str(e))
        

class MessageView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def list(self, request):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = serializer.data
            return Response(status=200, data=data)
        except Exception as e:
            error_message = str(e)
            return Response(status=404, data=error_message)
        
    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            serializer
            return Response(status=200 , data=serializer.data)

        except Exception as e:
            return Response(status=404, data=str(e))


