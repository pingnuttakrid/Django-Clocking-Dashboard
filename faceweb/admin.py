from django.contrib import admin
from faceweb.models import Employee,Clocking,Image_Clocking,Status,Threshold_Clocking

# Register your models here.
admin.site.register(Employee)
admin.site.register(Clocking)
admin.site.register(Image_Clocking)
admin.site.register(Status)
admin.site.register(Threshold_Clocking)
