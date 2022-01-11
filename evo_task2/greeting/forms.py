from .models import FullName
from django.forms import ModelForm, TextInput


class FullNameForm(ModelForm):
    class Meta:
        model = FullName
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name',
                'type': 'text',
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name',
                'type': 'text',
            }),
        }
