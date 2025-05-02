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

class SyllabusForm(forms.Form):
    SEMESTER_CHOICES = [
        ('1-1', '1st Year, 1st Semester'),
        ('1-2', '1st Year, 2nd Semester'),
        ('1-3', '1st Year, 3rd Semester'),
        ('2-1', '2nd Year, 1st Semester'),
        ('2-2', '2nd Year, 2nd Semester'),
        ('2-3', '2nd Year, 3rd Semester'),
        ('3-1', '3rd Year, 1st Semester'),
        ('3-2', '3rd Year, 2nd Semester'),
        ('3-3', '3rd Year, 3rd Semester'),
    ]

    major = forms.ModelChoiceField(queryset=Major.objects.all(), label="Specialty")
    semester = forms.ChoiceField(choices=SEMESTER_CHOICES, label="Semester")
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Course")
    syllabus_file = forms.FileField(label="Syllabus File", widget=forms.FileInput(attrs={'accept': '.doc,.docx'}))