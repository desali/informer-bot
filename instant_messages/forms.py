from django import forms


class InstantMessageCreateForm(forms.Form):
    project = forms.IntegerField()
    text = forms.CharField(required=True)
    url = forms.CharField(required=False)
    media = forms.ImageField(required=False)
    fields = ['text', 'url', 'media', 'project']
