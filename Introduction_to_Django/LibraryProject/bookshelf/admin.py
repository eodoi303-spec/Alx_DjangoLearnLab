from django.contrib import admin

# Register your models here.from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Book model.
    
    Features:
    - Displays title, author, and publication_year in list view
    - Adds filters for author and publication_year
    - Enables search functionality for title and author
    """
    
    # Display these columns in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filter sidebar for these fields
    list_filter = ('author', 'publication_year')
    
    # Enable search for these fields
    search_fields = ('title', 'author')


# Register the Book model with custom admin class
admin.site.register(Book, BookAdmin)

