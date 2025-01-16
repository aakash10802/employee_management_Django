from django.shortcuts import render
from .models import employee
from .forms import employeeForm
# Create your views here.


def success_function(request):
    return render(request,"success.html")

def home(request):
    return render(request,"home.html")
def employee_list(request):
    if request.method=="POST":
        s=employeeForm(request.POST)
        if s.is_valid():
            s.save()
            return render(success_function)
    
    
    x=employeeForm()
    return render(request,"employee_list.html",{"view":x})
