from django.contrib import admin

from tmessages.models import Message

message_models = [Message]
admin.site.register(message_models)
