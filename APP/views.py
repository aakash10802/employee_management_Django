from django.shortcuts import render,redirect
from .models import employee
from .forms import employeeForm
# Create your views here.


def success_function(request):
    return render(request,"success.html")

def home(request):
    return render(request,"home.html")

def employee_function(request):
    if request.method=="POST":
        s=employeeForm(request.POST)
        if s.is_valid():
            s.save()
            return redirect(success_function)
    else:
        x=employeeForm    
        return render(request,"employedetails.html",{"view":x})

def next_function(request):
    return render(request,'next.html')

def list_function(request):
    m=employee.objects.all()
    return render(request,'list.html',{'empt':m})