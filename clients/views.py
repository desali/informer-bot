from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from clients.serializers import ClientListSerializer
from projects.models import Project


class ClientListView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'clients/list.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        project = Project.objects.get(id=request.user.project.id)
        clients = project.clients
        clients_data = ClientListSerializer(clients, many=True).data

        return render(request, self.template_name, {
            'clients': clients_data
        })
