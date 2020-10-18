"""face URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from faceweb import views
import os
from django.contrib.auth.models import User
from faceweb.models import Employee

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

'''user=User.objects.all().latest('last_login')
email = user.email
profile = Employee.objects.all().filter(email=email)[0]
status_slug = profile.status.slug
slug = profile.slug'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/',views.signout,name="signOut"),
    path('',views.home,name="home"),
    path('index/',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('employees/',views.employees,name="employees"),
    path('status/<slug:status_slug>',views.employees,name='employee_by_status'),
    path('timesheet/',views.timesheet,name="timesheet"),
    path('timeline/',views.timeline,name="timeline"),
    path('employee/<slug:status_slug>/<slug:employee_slug>',views.employeePage,name='employee_detail'),
    #path('employee/{}/{}'.format(status_slug,slug),views.employeePage,name='employee_user'),
    path('employeeTable/<slug:slug>',views.employeeTable,name='employee_Table'),
       url(r'^rest/', include('faceweb.urls')),
       url(r'^image/', include('faceweb.urls')),	
]

if settings.DEBUG :
    # static/media
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    # static/
    urlpatterns+=static(settings.STATIC_URL,document_root=os.path.join(BASE_DIR,'static'))
    #static/media/employee/1.jpg