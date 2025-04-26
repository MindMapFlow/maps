from django import forms
from .models import Major, Course

class MajorForm(forms.ModelForm):
    class Meta:
        model = Major
        fields = ['name']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'major', 'semester']