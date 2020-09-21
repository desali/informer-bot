from rest_framework import serializers

from instant_messages.models import InstantMessage


class InstantMessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstantMessage
        fields = ['id', 'date']


class InstantMessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstantMessage
        fields = ['date', 'project']
