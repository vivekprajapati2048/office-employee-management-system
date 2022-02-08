from django.shortcuts import render
from .models import Department, Role, Employee

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    return render(request, 'view_all_emp.html', {
        "all_emps": emps
    })
    
def add_emp(request):
    return render(request, 'add_emp.html')

def remove_emp(request):
    return render(request, 'remove_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')
