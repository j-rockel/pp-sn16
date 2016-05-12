from django import forms

from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        deadline = forms.DateField(input_formats=['%d.%m.%Y', '%Y-%m-%d'])
        fields = ['content', 'deadline', 'progress']
