from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model

# Model representing a Tweet
class Tweet(models.Model):
    # ForeignKey creates a many-to-one relationship with the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    # Text content of the tweet (up to 240 characters)
    text = models.TextField(max_length=240)  
    # Optional image associated with the tweet
    image = models.ImageField(upload_to='photo/', blank=True, null=True)  

    # Automatically sets the field to the current timestamp when the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically updates the field to the current timestamp whenever the object is saved
    updated_at = models.DateTimeField(auto_now=True)  

    # String representation of the Tweet object
    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'

    # Meta options (optional)
    class Meta:
        ordering = ['-created_at']  # Order tweets by creation date, newest first
