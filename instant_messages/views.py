from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from instant_messages.forms import InstantMessageCreateForm
from instant_messages.serializers import InstantMessageListSerializer, InstantMessageCreateSerializer
from projects.models import Project
from tmessages.serializers import MessageCreateSerializer


class InstantMessageListView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'instant_messages/list.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        instant_messages = project.instant_messages
        instant_messages_data = InstantMessageListSerializer(instant_messages, many=True).data

        return render(request, self.template_name, {
            'instant_messages': instant_messages_data
        })


class InstantMessageCreateView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'instant_messages/create.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        instant_message_form = InstantMessageCreateForm()

        return render(request, self.template_name, {
            'form': instant_message_form
        })

    def post(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.POST['project'] = request.user.project.id
        request.POST['date'] = timezone.now()
        request.POST._mutable = True

        instant_message_form = InstantMessageCreateForm(request.POST, request.FILES)
        print(instant_message_form)

        if instant_message_form.is_valid():
            message_serializer = MessageCreateSerializer(data=instant_message_form.cleaned_data)
            assert message_serializer.is_valid()
            message = message_serializer.save()
            print(message_serializer.data)

            instant_message_serializer = InstantMessageCreateSerializer(data=instant_message_form.cleaned_data)
            assert instant_message_serializer.is_valid(raise_exception=True)
            instant_message = instant_message_serializer.save(message=message)

            if instant_message:
                return redirect('instant-message-list')
            else:
                return render(request, self.template_name, {
                    'form': instant_message_form
                })
        else:
            return render(request, self.template_name, {
                'form': instant_message_form
            })
