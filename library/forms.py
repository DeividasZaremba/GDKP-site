from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EventRegistration

class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EventRegistrationForm(forms.ModelForm):
    event_date = forms.DateTimeField(
        widget=forms.TextInput(attrs={'class': 'event-date-picker'})
    )

    class Meta:
        model = EventRegistration
        fields = ['event_name', 'event_date', 'event_info']


