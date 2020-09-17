from django.contrib import admin

from admins.models import Admin

admin_models = [Admin]
admin.site.register(admin_models)
