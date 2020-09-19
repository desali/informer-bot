from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from core.models import Hour
from daily_lessons.forms import DailyLessonCreateForm, DailyLessonEditForm
from daily_lessons.models import DailyLesson
from daily_lessons.serializers import DailyLessonListSerializer, DailyLessonEditSerializer
from projects.models import Project


class DailyLessonListView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'daily_lessons/list.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        daily_lessons = project.daily_lessons.order_by('day')
        daily_lessons_data = DailyLessonListSerializer(daily_lessons, many=True).data

        return render(request, self.template_name, {
            'daily_lessons': daily_lessons_data
        })


class DailyLessonCreateView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'daily_lessons/create.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        hours = Hour.objects.all()
        lessons = DailyLesson.objects.all().order_by('-day')
        last_lesson_day = lessons[0].day + 1 if lessons else 1
        lesson_form = DailyLessonCreateForm()

        return render(request, self.template_name, {
            'form': lesson_form,
            'hours': hours,
            'day': last_lesson_day
        })

    def post(self, request, *args, **kwargs):
        hours = Hour.objects.all()
        lessons = DailyLesson.objects.all().order_by('-day')
        last_lesson_day = lessons[0].day + 1 if lessons else 1

        request.POST._mutable = True
        request.POST['project'] = request.user.project.id
        request.POST['day'] = last_lesson_day
        request.POST._mutable = True

        lesson_form = DailyLessonCreateForm(request.POST)

        if lesson_form.is_valid():
            daily_lesson = lesson_form.save()
            if daily_lesson:
                return redirect('daily-lesson-list')
            else:
                return render(request, self.template_name, {
                    'form': lesson_form,
                    'hours': hours,
                    'day': last_lesson_day
                })
        else:
            return render(request, self.template_name, {
                'form': lesson_form,
                'hours': hours,
                'day': last_lesson_day
            })


class DailyLessonUpdateView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'daily_lessons/edit.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        hours = Hour.objects.all()
        project = Project.objects.get(id=request.user.project.id)
        daily_lesson = DailyLesson.objects.get(id=kwargs.get('id'), project=project)
        lesson_form = DailyLessonEditForm(DailyLessonEditSerializer(daily_lesson).data)

        return render(request, self.template_name, {
            'form': lesson_form,
            'hours': hours,
            'day': daily_lesson.day
        })

    def post(self, request, *args, **kwargs):
        hours = Hour.objects.all()
        project = Project.objects.get(id=request.user.project.id)
        daily_lesson = DailyLesson.objects.get(id=kwargs.get('id'), project=project)
        lesson_form = DailyLessonEditForm(request.POST)

        if lesson_form.is_valid():
            title = lesson_form.cleaned_data['title']
            hour = lesson_form.cleaned_data['hour']

            daily_lesson.title = title
            daily_lesson.hour = hour
            daily_lesson.save()

            if daily_lesson:
                return redirect('daily-lesson-list')
            else:
                return render(request, self.template_name, {
                    'form': lesson_form,
                    'hours': hours,
                    'day': daily_lesson.day
                })
        else:
            return render(request, self.template_name, {
                'form': lesson_form,
                'hours': hours,
                'day': daily_lesson.day
            })


class DailyLessonDeleteView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        daily_lesson = DailyLesson.objects.get(id=kwargs.get('id'), project=project)
        daily_lesson.delete()

        return redirect('daily-lesson-list')
