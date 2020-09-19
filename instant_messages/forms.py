from django import forms


class InstantMessageCreateForm(forms.Form):
    date = forms.DateTimeField()
    project = forms.IntegerField()
    text = forms.CharField(required=True)
    url = forms.CharField(required=False)
    media = forms.ImageField(required=False)
    fields = ['date', 'text', 'url', 'media', 'project']
