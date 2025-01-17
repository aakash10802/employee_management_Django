from django import forms # type: ignore
from .models import employee

class employeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = "__all__"
        