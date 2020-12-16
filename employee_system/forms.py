from django import forms
from .models import Employee
from crispy_forms.helper import FormHelper

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name','last_name','gender','birth_date','email','mobile','hire_date','employee_type','photo']
