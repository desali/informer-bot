from django.contrib import admin

from core.models import Timing

core_models = [Timing]
admin.site.register(core_models)
