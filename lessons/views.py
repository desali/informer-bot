from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from lessons.forms import LessonCreateForm, LessonEditForm
from lessons.models import Lesson
from lessons.serializers import LessonListSerializer, LessonEditSerializer
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


class LessonCreateView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'lessons/create.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        lesson_form = LessonCreateForm()

        return render(request, self.template_name, {
            'form': lesson_form
        })

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['project'] = request.user.project.id
        request.POST._mutable = True

        lesson_form = LessonCreateForm(request.POST)

        if lesson_form.is_valid():
            lesson = lesson_form.save()
            if lesson:
                return redirect('lesson-list')
            else:
                return render(request, self.template_name, {
                    'form': lesson_form
                })
        else:
            return render(request, self.template_name, {
                'form': lesson_form
            })


class LessonUpdateView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'lessons/edit.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        lesson = Lesson.objects.get(id=kwargs.get('id'), project=project)
        lesson_form = LessonEditForm(LessonEditSerializer(lesson).data)

        return render(request, self.template_name, {
            'form': lesson_form
        })

    def post(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        lesson = Lesson.objects.get(id=kwargs.get('id'), project=project)
        lesson_form = LessonEditForm(request.POST)

        if lesson_form.is_valid():
            title = lesson_form.cleaned_data['title']
            date = lesson_form.cleaned_data['date']

            lesson.title = title
            lesson.date = date
            lesson.save()

            if lesson:
                return redirect('lesson-list')
            else:
                return render(request, self.template_name, {
                    'form': lesson_form
                })
        else:
            return render(request, self.template_name, {
                'form': lesson_form
            })


class LessonDeleteView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        lesson = Lesson.objects.get(id=kwargs.get('id'), project=project)
        lesson.delete()

        return redirect('lesson-list')
