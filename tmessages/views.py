from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from projects.models import Project
from tmessages.forms import MessageEditForm
from tmessages.models import Message
from tmessages.serializers import MessageSerializer, MessageEditSerializer


class MessageDetailView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'tmessages/detail.html'

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        message = Message.objects.get(id=kwargs.get('id'), project=project)
        message_data = MessageSerializer(message).data

        if request.GET.get('next') == 'lesson-timed-message-list':
            lesson_id = message.lesson_timed.lesson.id
        elif request.GET.get('next') == 'daily-lesson-timed-message-list':
            lesson_id = message.daily_lesson_timed.lesson.id
        else:
            lesson_id = None

        return render(request, self.template_name, {
            'message': message_data,
            'from': request.GET.get('next'),
            'id': lesson_id
        })

    redirect_field_name = ''


class MessageUpdateView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'tmessages/edit.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        message = Message.objects.get(id=kwargs.get('id'), project=project)
        message_form = MessageEditForm(MessageEditSerializer(message).data)

        return render(request, self.template_name, {
            'form': message_form,
            'from': request.GET.get('next')
        })

    def post(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        message = Message.objects.get(id=kwargs.get('id'), project=project)
        message_form = MessageEditForm(request.POST, request.FILES)
        if request.GET.get('next') == 'lesson-timed-message-list':
            lesson_id = message.lesson_timed.lesson.id
        elif request.GET.get('next') == 'daily-lesson-timed-message-list':
            lesson_id = message.daily_lesson_timed.lesson.id
        else:
            lesson_id = None

        if message_form.is_valid():
            text = message_form.cleaned_data['text']
            url = message_form.cleaned_data['url']
            media = message_form.cleaned_data['media']

            message.text = text
            message.url = url
            if media:
                message.media = media

            message.save()

            if message:
                if lesson_id:
                    return redirect(request.POST.get('next'), id=lesson_id)
                else:
                    return redirect(request.POST.get('next'))
            else:
                return render(request, self.template_name, {
                    'form': message_form,
                    'from': request.POST.get('next')
                })
        else:
            return render(request, self.template_name, {
                'form': message_form,
                'from': request.POST.get('next')
            })
