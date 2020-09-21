from rest_framework import serializers

from tmessages.models import Message, WelcomeMessage, ConfirmMessage


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'text', 'url', 'media']


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text', 'url', 'media']


class MessageEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'text', 'url', 'media']


class WelcomeMessageSerializer(serializers.ModelSerializer):
    message = MessageSerializer()

    class Meta:
        model = WelcomeMessage
        fields = ['message']


class ConfirmMessageSerializer(serializers.ModelSerializer):
    message = MessageSerializer()

    class Meta:
        model = ConfirmMessage
        fields = ['message']
