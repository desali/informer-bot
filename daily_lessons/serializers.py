from rest_framework import serializers

from daily_lessons.models import DailyLesson


class DailyLessonListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    hour = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = DailyLesson
        fields = ['id', 'title', 'day', 'hour', 'message', 'status']


class DailyLessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLesson
        fields = ['title', 'hour']


class DailyLessonEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLesson
        fields = ['title', 'hour']
