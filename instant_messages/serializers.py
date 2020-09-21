from rest_framework import serializers

from instant_messages.models import InstantMessage


class InstantMessageListSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = InstantMessage
        fields = ['id', 'date', 'message']

    def get_date(self, instance_message):
        return instance_message.date.strftime('%d/%m/%Y, %H:%M')


class InstantMessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstantMessage
        fields = ['project']
