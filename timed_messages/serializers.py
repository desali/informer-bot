from rest_framework import serializers

from timed_messages.models import LessonTimedMessage, DailyLessonTimedMessage


class LessonTimedMessageListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    timing = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = LessonTimedMessage
        fields = ['id', 'timing', 'status', 'message']


class DailyLessonTimedMessageListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    timing = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = DailyLessonTimedMessage
        fields = ['id', 'timing', 'status', 'message']
