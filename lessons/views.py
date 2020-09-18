from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from lessons.forms import LessonEditForm
from lessons.models import Lesson
from lessons.serializers import LessonListSerializer
from projects.models import Project


class LessonListView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'lessons/list.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        lessons = project.lessons
        lessons_data = LessonListSerializer(lessons, many=True).data

        return render(request, self.template_name, {
            'lessons': lessons_data
        })


class LessonEditView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'lessons/edit.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        lesson = Lesson.objects.get(id=request.data.get('id'), project=project)

        lesson_form = LessonEditForm(lesson)

        return render(request, self.template_name, {
            'form': lesson_form
        })
