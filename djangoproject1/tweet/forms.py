from django import forms
from django.contrib.auth.models import User

from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class FormTweet(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'image']  # Fields to include in the form
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'id': 'id_text',  # Custom ID for targeting in CSS
                    'placeholder': 'Write your thoughts here...',  # Placeholder text
                    'style': 'height: 250px; resize: vertical; font-size: 18px; width: 100%;'
                }
            )
        }
        labels = {
            'text': 'Text',
            'image': 'Image'
        }
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

