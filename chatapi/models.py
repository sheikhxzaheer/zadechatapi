from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    chat_name = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return self.chat_name
    

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message = models.CharField(max_length=50, null=False, default='')

    def __str__(self):
        return self.message
    