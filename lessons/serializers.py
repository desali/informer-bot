from rest_framework import serializers

from lessons.models import Lesson


class LessonListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Lesson
        fields = ['id', 'title', 'date', 'status', 'message']
