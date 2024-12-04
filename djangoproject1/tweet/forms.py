from django import form
from .models import Tweet 

class FormTweet():
    class Meta:
        model= Tweet
        fields =['text', 'image ']