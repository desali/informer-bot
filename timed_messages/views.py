from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from core.models import Timing
from daily_lessons.models import DailyLesson
from lessons.models import Lesson
from projects.models import Project
from timed_messages.forms import LessonTimedMessageCreateForm, DailyLessonTimedMessageCreateForm
from timed_messages.models import LessonTimedMessage, DailyLessonTimedMessage
from timed_messages.serializers import LessonTimedMessageListSerializer, DailyLessonTimedMessageListSerializer
from tmessages.models import Message


class LessonTimedMessageListView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'timed_messages/lesson_list.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        lesson = Lesson.objects.get(id=kwargs.get('id'), project=project)
        timed_messages = lesson.timed_messages.order_by('timing')
        timed_messages_data = LessonTimedMessageListSerializer(timed_messages, many=True).data

        return render(request, self.template_name, {
            'timed_messages': timed_messages_data,
            'id': lesson.id
        })


class LessonTimedMessageCreateView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'timed_messages/lesson_create.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        lesson = Lesson.objects.get(id=kwargs.get('id'), project=project)
        timed_message_form = LessonTimedMessageCreateForm()
        timings = Timing.objects.exclude(id__in=lesson.timed_messages.values('timing'))

        return render(request, self.template_name, {
            'form': timed_message_form,
            'timings': timings,
            'id': lesson.id
        })

    def post(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        lesson = Lesson.objects.get(id=kwargs.get('id'), project=project)

        request.POST._mutable = True
        request.POST['lesson'] = lesson.id
        request.POST._mutable = True

        timed_message_form = LessonTimedMessageCreateForm(request.POST)

        if timed_message_form.is_valid():
            message = Message()
            message.text = "Test title"
            message.project = project
            message.save()

            timed_message_form.instance.message = message
            timed_message = timed_message_form.save()
            if timed_message:
                return redirect('lesson-timed-message-list', id=lesson.id)
            else:
                return render(request, self.template_name, {
                    'form': timed_message_form,
                    'id': lesson.id
                })
        else:
            return render(request, self.template_name, {
                'form': timed_message_form,
                'id': lesson.id
            })


class LessonTimedMessageDeleteView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        lesson = Lesson.objects.get(id=kwargs.get('id'), project=project)
        timed_message = LessonTimedMessage.objects.get(id=kwargs.get('tmid'), lesson=lesson)
        timed_message.delete()

        return redirect('lesson-timed-message-list', id=lesson.id)


class DailyLessonTimedMessageListView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'timed_messages/daily_lesson_list.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        lesson = DailyLesson.objects.get(id=kwargs.get('id'), project=project)
        timed_messages = lesson.timed_messages.order_by('timing')
        timed_messages_data = DailyLessonTimedMessageListSerializer(timed_messages, many=True).data

        return render(request, self.template_name, {
            'timed_messages': timed_messages_data,
            'id': lesson.id
        })


class DailyLessonTimedMessageCreateView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'timed_messages/daily_lesson_create.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        lesson = DailyLesson.objects.get(id=kwargs.get('id'), project=project)
        timed_message_form = DailyLessonTimedMessageCreateForm()
        timings = Timing.objects.exclude(id__in=lesson.timed_messages.values('timing'))

        return render(request, self.template_name, {
            'form': timed_message_form,
            'timings': timings,
            'id': lesson.id
        })

    def post(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        lesson = DailyLesson.objects.get(id=kwargs.get('id'), project=project)

        request.POST._mutable = True
        request.POST['daily_lesson'] = lesson.id
        request.POST._mutable = True

        timed_message_form = DailyLessonTimedMessageCreateForm(request.POST)

        if timed_message_form.is_valid():
            message = Message()
            message.text = "Test title"
            message.project = project
            message.save()

            timed_message_form.instance.message = message
            timed_message = timed_message_form.save()
            if timed_message:
                return redirect('daily-lesson-timed-message-list', id=lesson.id)
            else:
                return render(request, self.template_name, {
                    'form': timed_message_form,
                    'id': lesson.id
                })
        else:
            return render(request, self.template_name, {
                'form': timed_message_form,
                'id': lesson.id
            })


class DailyLessonTimedMessageDeleteView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        lesson = DailyLesson.objects.get(id=kwargs.get('id'), project=project)
        timed_message = DailyLessonTimedMessage.objects.get(id=kwargs.get('tmid'), lesson=lesson)
        timed_message.delete()

        return redirect('daily-lesson-timed-message-list', id=lesson.id)
