from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone_number', 'salary', 'designation', 'description']
        widgets = {
            'salary': forms.TextInput(attrs={'readonly': 'readonly'}),
            'designation': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
