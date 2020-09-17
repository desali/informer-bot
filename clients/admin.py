from django.contrib import admin

from clients.models import Client

client_models = [Client]
admin.site.register(client_models)
