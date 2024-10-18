from django import forms
from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'})
        }


class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()