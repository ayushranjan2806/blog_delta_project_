from django.contrib import admin
from .models import Tweet

class TweetAdmin(admin.ModelAdmin):
    # Specify which fields to display in the admin list view
    list_display = ('user', 'text', 'created_at', 'updated_at', 'image')

    # Add search functionality by user and tweet text
    search_fields = ('user__username', 'text')

    # Add filters for date fields and user
    list_filter = ('created_at', 'updated_at', 'user')

    # Allow editing tweets directly in the admin interface
    fields = ('user', 'text', 'image')  # Fields to display on the edit page
    readonly_fields = ('created_at', 'updated_at')  # Make created_at and updated_at read-only

    # Optionally, you can also add ordering to list the latest tweets at the top
    ordering = ('-created_at',)  # Show the latest tweets first

# Register the custom TweetAdmin with the Tweet model
admin.site.register(Tweet, TweetAdmin)
