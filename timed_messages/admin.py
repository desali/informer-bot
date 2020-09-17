from django.contrib import admin

from timed_messages.models import TimedMessage

timed_message_models = [TimedMessage]
admin.site.register(timed_message_models)
