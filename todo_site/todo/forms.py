from django import forms
from .models import TodoItem  # Ensure this matches the model name

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem  # Use TodoItem here
        fields = "__all__"
