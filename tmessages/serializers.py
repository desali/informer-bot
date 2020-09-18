from rest_framework import serializers

from tmessages.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'text', 'url', 'media']
