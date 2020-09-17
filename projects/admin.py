from django.contrib import admin

from projects.models import Project

project_models = [Project]
admin.site.register(project_models)