from django.contrib import admin
from .models import TodoItem  # Corrected import

# Register your models here.
admin.site.register(TodoItem)
