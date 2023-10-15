from django import forms
from .models import NewStudents

class NewStudentForm(forms.ModelForm):
    class Meta:
        model = NewStudents
        fields = '__all__'