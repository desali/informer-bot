from django.contrib import admin

from lessons.models import Lesson

lesson_models = [Lesson]
admin.site.register(lesson_models)
