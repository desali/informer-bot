from django.contrib import admin

from core.models import Timing, Hour

core_models = [Timing, Hour]
admin.site.register(core_models)
