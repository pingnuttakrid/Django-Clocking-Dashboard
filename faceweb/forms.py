from faceweb.models import Employee,Threshold_Clocking
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('title','firstname','lastname','email','status','Type','contact','adresss','adcontact','overseaadresss','ovcontact','emerseaadresss','emercontact')
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('imgprofile','imgstraight','imgtop','imgbottom','imgleft','imgright')


