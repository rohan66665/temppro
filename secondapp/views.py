from django.shortcuts import render
from django.http import HttpResponse
from secondapp.models import Employee
import datetime
from django.shortcuts import render
from.import forms



def display(request):
    msg="<h1> WELCOME TO DJANGO CODING </h1>"
    return HttpResponse(msg)

def wish(request):
    date=datetime.datetime.now()
    msg="All is not well"
    my_dict={'insert_date':date,'insert_msg':msg}
    return render(request,'secondapp/rohan.html',context=my_dict)

def empdata(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request, 'secondapp/emp.html', context=my_dict)

def studentinputview(request):
   form=forms.StudentForm()
   my_dict={'form':form}
   return render(request,'secondapp/input.html',context=my_dict)