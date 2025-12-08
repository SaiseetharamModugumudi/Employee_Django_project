from django import forms
from app1.models import Employee

class Employee_Form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'