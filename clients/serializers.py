from rest_framework import serializers

from clients.models import Client


class ClientListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Client
        fields = ['id', 'phone', 'status']
