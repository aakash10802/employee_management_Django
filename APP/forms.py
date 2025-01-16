from django import forms
from .models import employee

class employeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = "__all__"