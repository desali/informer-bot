from django.contrib import admin

from core.models import Timing, Hour, Minute

core_models = [Timing, Hour, Minute]
admin.site.register(core_models)
