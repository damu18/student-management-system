from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'roll_number',
            'email',
            'mobile_no',
            'date_of_birth',
            'gender',
            'class_name',
            'marks',
            'address'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'e.g. John'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'e.g. Doe'}),
            'roll_number': forms.TextInput(attrs={'placeholder': 'e.g. STU1001'}),
            'email': forms.EmailInput(attrs={'placeholder': 'e.g. john.doe@example.com'}),
            'mobile_no': forms.TextInput(attrs={'placeholder': 'e.g. +1234567890'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(),
            'class_name': forms.TextInput(attrs={'placeholder': 'e.g. Grade 10-A'}),
            'marks': forms.NumberInput(attrs={'placeholder': 'e.g. 95.50', 'step': '0.01', 'min': '0', 'max': '100'}),
            'address': forms.Textarea(attrs={'placeholder': 'e.g. 123 Main St, New York, NY', 'rows': 3}),
        }
