from rest_framework import serializers

from projects.models import Project
from tmessages.serializers import ConfirmMessageSerializer, WelcomeMessageSerializer


class ProjectSerializer(serializers.ModelSerializer):
    welcome_message = WelcomeMessageSerializer()
    confirm_message = ConfirmMessageSerializer()

    lessons = serializers.SerializerMethodField()
    daily_lessons = serializers.SerializerMethodField()
    clients = serializers.SerializerMethodField()
    instant_messages = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['title', 'confirm_message', 'welcome_message', 'lessons', 'clients', 'daily_lessons',
                  'instant_messages']

    def get_lessons(self, project):
        return project.lessons.count()

    def get_daily_lessons(self, project):
        return project.daily_lessons.count()

    def get_clients(self, project):
        return project.clients.count()

    def get_instant_messages(self, project):
        return project.instant_messages.count()
