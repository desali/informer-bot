from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from projects.models import Project
from tmessages.models import Message
from tmessages.serializers import MessageSerializer


class MessageDetailView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'tmessages/detail.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        message = Message.objects.get(id=kwargs.get('id'), project=project)
        message_data = MessageSerializer(message).data

        return render(request, self.template_name, {
            'message': message_data
        })


# class MessageUpdateView(LoginRequiredMixin, View):
#     login_url = '/auth/login/'
#     template_name = 'tmessages/edit.html'
#     redirect_field_name = ''
#
#     def get(self, request, *args, **kwargs):
#         hours = Hour.objects.all()
#         project = Project.objects.get(id=request.user.project.id)
#         daily_lesson = DailyLesson.objects.get(id=kwargs.get('id'), project=project)
#         lesson_form = DailyLessonEditForm(DailyLessonEditSerializer(daily_lesson).data)
#
#         return render(request, self.template_name, {
#             'form': lesson_form,
#             'hours': hours,
#             'day': daily_lesson.day
#         })
#
#     def post(self, request, *args, **kwargs):
#         hours = Hour.objects.all()
#         project = Project.objects.get(id=request.user.project.id)
#         daily_lesson = DailyLesson.objects.get(id=kwargs.get('id'), project=project)
#         lesson_form = DailyLessonEditForm(request.POST)
#
#         if lesson_form.is_valid():
#             title = lesson_form.cleaned_data['title']
#             hour = lesson_form.cleaned_data['hour']
#
#             daily_lesson.title = title
#             daily_lesson.hour = hour
#             daily_lesson.save()
#
#             if daily_lesson:
#                 return redirect('daily-lesson-list')
#             else:
#                 return render(request, self.template_name, {
#                     'form': lesson_form,
#                     'hours': hours,
#                     'day': daily_lesson.day
#                 })
#         else:
#             return render(request, self.template_name, {
#                 'form': lesson_form,
#                 'hours': hours,
#                 'day': daily_lesson.day
#             })
