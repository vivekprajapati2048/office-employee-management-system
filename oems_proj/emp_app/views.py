from datetime import datetime
from django.http import HttpResponse
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
    
    if request.method == 'POST':
        first_name =  request.POST['first_name']
        last_name =  request.POST['last_name']
        salary =  int(request.POST['salary'])
        bonus =  int(request.POST['bonus'])
        phone =  int(request.POST['phone'])
        department =  request.POST['department']
        role =  request.POST['role']
        
        new_employee = Employee(first_name=first_name, last_name=last_name, 
                 phone=phone, salary=salary, bonus=bonus,
                 role_id=role, dept_id=department,
                 hire_date=datetime.now())
        
        new_employee.save()
        return HttpResponse('Employee added Successfully!')
    
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    
    else:
        return HttpResponse('An Exception Occured! Employee has not been added!')

def remove_emp(request):
    return render(request, 'remove_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')
