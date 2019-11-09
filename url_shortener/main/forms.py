from django import forms
from .models import UserUrl


class UrlForm(forms.ModelForm):

    class Meta:
        model = UserUrl
        fields = ['long_url']
