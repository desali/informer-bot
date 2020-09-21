from rest_framework import serializers

from timed_messages.models import LessonTimedMessage
from tmessages.serializers import MessageSerializer


class LessonTimedMessageListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    timing = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = LessonTimedMessage
        fields = ['id', 'timing', 'status', 'message']
