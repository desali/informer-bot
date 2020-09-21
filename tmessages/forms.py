from django.forms import ModelForm

from tmessages.models import Message


class MessageEditForm(ModelForm):
    class Meta:
        model = Message
        fields = ['id', 'text', 'media', 'url']
