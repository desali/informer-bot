from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectView(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    template_name = 'projects/home.html'
    redirect_field_name = ''

    def get(self, request, *args, **kwargs):
        print(request.user.project)

        project = Project.objects.get(id=request.user.project.id)
        project_data = ProjectSerializer(project).data

        return render(request, self.template_name, {
            'project': project_data
        })


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
