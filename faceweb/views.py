from django.shortcuts import render,get_object_or_404,redirect
from .serializers import ClockingSerializer,imageSerializer
from rest_framework.generics import (CreateAPIView)
from faceweb.models import Clocking,Image_Clocking,Employee,Status
from django.contrib.auth import login , authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import F, Max
import datetime
from .filters import ClockingFilter
from .forms import EmployeeForm,ImageForm

# Create your views here.
class ClockingCreateAPIView(CreateAPIView):
    serializer_class = ClockingSerializer
    queryset = Clocking.objects.all()
    lookup_field = 'id'

class ImageCreateAPIView(CreateAPIView):
	serializer_class = imageSerializer
	queryset = Image_Clocking.objects.all()


def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect('index')
        else :
            messages.error(request,'username or password not correct')
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request,'home.html',{'form':form})

@login_required(login_url='home')
def signout(request):
    logout(request)
    return redirect('home') 

@login_required(login_url='home')
def index(request):
    return render(request,'index.html')


@login_required(login_url='home')
def employees(request,status_slug=None):
    employees = None
    status_page = None
    if status_slug != None:
         status_page = get_object_or_404(Status,slug=status_slug)
         employees = Employee.objects.all().filter(status=status_page)
    else:
        employees = Employee.objects.all().filter()
    
    return render(request,'employees.html',{'employees':employees,'status':status_page})


@login_required(login_url='home')
def timesheet(request):
    clocking = None
    clocking = Clocking.objects.order_by('employee_id', '-datetime').distinct('employee_id')
    date = datetime.date.today()
    clocking_filter = ClockingFilter(request.GET,queryset=clocking)
    clocking = clocking_filter.qs
    
    return render(request,'timesheet.html',{'clockings':clocking,'date':date,'filter':clocking_filter})


@login_required(login_url='home')
def employeePage(request,status_slug,employee_slug):
    try:
        employee = Employee.objects.get(status__slug=status_slug,slug=employee_slug)
    except Exception as e:
        raise e      
    form_class = EmployeeForm 
    form_image = ImageForm
    
    if request.method == 'POST':
        print(request.POST )
        if 'imgprofile' or 'imgright' or 'imgleft' or 'imgtop' or 'imgbottom' or 'imgstraight' in request.headers:
            form_image = form_image(data=request.POST, files=request.FILES,instance=employee)
            if form_image.is_valid():
                form_image.save()
                return redirect('employee_detail',status_slug=status_slug,employee_slug=employee_slug)
        else:
            form = form_class(data=request.POST,instance=employee)
            status=request.POST.getlist('status')
            status_id =status[0]
            status = Status.objects.values('slug').get(id=status_id)
            status_slug = status.get("slug")
            if form.is_valid():
                form.save()
                return redirect('employee_detail',status_slug=status_slug,employee_slug=employee_slug)    
    else:
        form_image = form_image(instance=employee)
        form = form_class(instance=employee)
    
    
    return render(request,'employee.html',{'employee':employee,'form':form,'form_image':form_image})


@login_required(login_url='home')
def employeeTable(request,slug):
    employee = None
    employee_id = None
    clocking = None
    employee_id = Employee.objects.filter(slug=slug).order_by('-id')[0]
    clocking = Clocking.objects.filter(employee_id=employee_id)    
    employee = Employee.objects.all().filter(slug=slug)
    clocking_filter = ClockingFilter(request.GET,queryset=clocking)
    clocking = clocking_filter.qs 
    
    return render(request,'employeeTable.html',{'clockings':clocking,'employee':employee,'filter':clocking_filter})