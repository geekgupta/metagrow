from django import forms
from .models import Student, Subject

class StudentForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Student
        fields = ('name', 'age', 'roll_number', 'subjects')
        
        
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('name',)