from rest_framework import serializers

from clients.models import Client
from instant_messages.models import InstantMessage


class InstantMessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstantMessage
        fields = ['id', 'date']


class InstantMessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstantMessage
        fields = ['date', 'project']
