from django.shortcuts import render
from dbApp.models import Employee
# Create your views here.

def empDetails(request):
    emp_data = Employee.objects.all()
    emp_dict = {'emp_list':emp_data}
    return render(request,'dbApp/abc.html',context=emp_dict)
    