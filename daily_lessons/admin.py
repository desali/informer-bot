from django.contrib import admin

from daily_lessons.models import DailyLesson

daily_lesson_models = [DailyLesson]
admin.site.register(daily_lesson_models)
