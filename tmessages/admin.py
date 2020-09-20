from django.contrib import admin

from tmessages.models import Message, ConfirmMessage, WelcomeMessage

message_models = [Message, WelcomeMessage, ConfirmMessage]
admin.site.register(message_models)
