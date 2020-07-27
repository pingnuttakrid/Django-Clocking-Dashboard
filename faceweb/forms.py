from faceweb.models import Employee
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('firstname','lastname','email','status','Type')
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('imgprofile','imgstraight','imgtop','imgbottom','imgleft','imgright')


