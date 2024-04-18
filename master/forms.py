from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['user', 'standard', 'murshid', 'parent']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'standard': forms.Select(attrs={'class': 'form-control'}),
            'murshid': forms.Select(attrs={'class': 'form-control'}),
            'parent': forms.TextInput(attrs={'class': 'form-control'}),
        }
