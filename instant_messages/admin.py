from django.contrib import admin

from instant_messages.models import InstantMessage

instant_message_models = [InstantMessage]
admin.site.register(instant_message_models)
