from django import forms
from django.forms import ModelForm

from todolist.models import Task


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]

    title = forms.CharField(min_length=1, max_length=255)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 6, 'style': 'resize: none;'})
    )

    def save(self, user_id, commit=True):
        task = super().save(commit=False)
        task.user_id = user_id
        if commit:
            task.save()

        return task
