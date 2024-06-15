from django.contrib import admin
from .models import *

class chatAdmin(admin.ModelAdmin):
    display = ('chat_name')
class messageAdmin(admin.ModelAdmin):
    display = ('chat_name')

admin.site.register(Chat, chatAdmin)
admin.site.register(Message, messageAdmin)
