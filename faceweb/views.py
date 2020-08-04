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
import os
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
    clocking = Clocking.objects.annotate(most_recent=Max('employee_id__clocking__datetime')).filter(datetime=F('most_recent'))
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
    
    if request.method == 'POST' and 'btnform1' in request.POST:
       
        form_image = form_image(data=request.POST, files=request.FILES,instance=employee)
        if form_image.is_valid():
            form_image.save()
            return redirect('employee_detail',status_slug=status_slug,employee_slug=employee_slug)
    
    elif request.method=='POST' and 'btnform2' in request.POST:
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



@login_required(login_url='home')
def register(request):
    if request.method == "POST":  
        employee_id = request.POST["employee_id"]
        title = request.POST["title"]
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        nation = request.POST["nation"]
        Type = request.POST["Type"]
        idno = request.POST["idno"]
        idtype = request.POST["idtype"]
        birthday = request.POST["birthday"]
        contact = request.POST["contact"]
        addresss = request.POST["adresss"]
        adcontact = request.POST["adcontact"]
        overseaadresss = request.POST["overseaadresss"]
        ovcontact = request.POST["ovcontact"]
        emerseaadresss = request.POST["emerseaadresss"]
        emercontact = request.POST["emercontact"]
        
        imgprofile = request.FILES["imgprofile"]

        user_folder = 'static/media/employee/' + str(employee_id)
        if not os.path.exists(user_folder):
               os.mkdir(user_folder)
       
        imgprofile_extension = '{}-profiles.JPG'.format(employee_id)
        imgprofile_save_path = "{}/{}".format(user_folder, imgprofile_extension)
        with open(imgprofile_save_path, 'wb+') as f:
            for chunk in imgprofile.chunks():
                f.write(chunk)
        
        imgprofile_path = 'employee/{}/{}'.format(employee_id,imgprofile_extension)
        
        imgstraight = request.FILES["imgstraight"]
       
        imgstraight_extension = '{}-straight.JPG'.format(employee_id)
        imgstraight_save_path = "{}/{}".format(user_folder,imgstraight_extension)
        with open(imgstraight_save_path, 'wb+') as f:
            for chunk in imgstraight.chunks():
                f.write(chunk)
                
        imgstraight_path = 'employee/{}/{}'.format(employee_id,imgstraight_extension)
        
        imgtop = request.FILES["imgtop"]
        
        imgtop_extension = '{}-top.JPG'.format(employee_id)
        imgtop_save_path = "{}/{}".format(user_folder,imgtop_extension)
        with open(imgtop_save_path, 'wb+') as f:
            for chunk in imgtop.chunks():
                f.write(chunk)
        
        imgtop_path = 'employee/{}/{}'.format(employee_id,imgtop_extension)
        
        imgbottom = request.FILES["imgbottom"]
        
        imgbottom_extension = '{}-bottom.JPG'.format(employee_id)
        imgbottom_save_path = "{}/{}".format(user_folder,imgbottom_extension)
        with open(imgbottom_save_path, 'wb+') as f:
            for chunk in imgbottom.chunks():
                f.write(chunk)
                
        imgbottom_path = 'employee/{}/{}'.format(employee_id,imgbottom_extension)        
        
        imgleft = request.FILES["imgleft"]

        imgleft_extension = '{}-left.JPG'.format(employee_id)
        imgleft_save_path = "{}/{}".format(user_folder,imgleft_extension)
        with open(imgleft_save_path, 'wb+') as f:
            for chunk in imgleft.chunks():
                f.write(chunk)
        
        imgleft_path = 'employee/{}/{}'.format(employee_id,imgleft_extension) 
        
        imgright = request.FILES["imgright"]
        
        imgright_extension = '{}-right.JPG'.format(employee_id)
        imgright_save_path = "{}/{}".format(user_folder,imgright_extension)
        with open(imgright_save_path, 'wb+') as f:
            for chunk in imgright.chunks():
                f.write(chunk)
       
        imgright_path = 'employee/{}/{}'.format(employee_id,imgright_extension) 
        
        slug = firstname+lastname
        status = "1"
        
        employee = Employee(employee_id=employee_id,title=title,firstname=firstname,lastname=lastname,slug=slug,status_id=status,email=email,gender=gender,nation=nation,Type=Type,idno=idno,idtype=idtype,birthday=birthday,contact=contact,adresss=addresss,adcontact=adcontact,overseaadresss=overseaadresss,ovcontact=ovcontact,emerseaadresss=emerseaadresss,emercontact=emercontact,imgprofile=imgprofile_path,imgstraight=imgstraight_path,imgtop=imgtop_path,imgbottom=imgbottom_path,imgleft=imgleft_path,imgright=imgright_path)
        employee.save()
          
        return redirect('index')  
               

    return render(request,'register.html')

@login_required(login_url='home')
def timeline(request):
     
     now = datetime.datetime.now()
     
     year = now.year
     day = now.strftime("%A")
     date = now.strftime("%d")
     month = now.strftime("%B")
     
     return render(request,'timeline.html',{'year':year,'day':day,'date':date,'month':month})