from django.db import models
from django.urls import reverse
# Create your models here.
class Status(models.Model):
      name = models.CharField(max_length=255)
      slug = models.SlugField(max_length=255)
    
      def __str__(self):
           return self.name 

      def get_url(self):
         return reverse('employee_by_status',args=[self.slug])

class Employee(models.Model):
      title = models.CharField(max_length= 5 )
      employee_id = models.CharField(max_length=5)
      firstname = models.CharField(max_length=255)
      lastname = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      slug = models.SlugField(max_length=255)
      gender = models.CharField(max_length=10)
      nation = models.CharField(max_length=20)
      status = models.ForeignKey(Status,on_delete=models.CASCADE)
      Type = models.CharField(max_length=30)
      idtype = models.CharField(max_length=255)
      idno = models.CharField(max_length=13)
      birthday = models.CharField(max_length=255)
      contact = models.CharField(max_length=10)
      adresss =  models.CharField(max_length=300)
      adcontact = models.CharField(max_length=10)
      overseaadresss =  models.CharField(max_length=300)
      ovcontact = models.CharField(max_length=10)
      emerseaadresss =  models.CharField(max_length=300)
      emercontact = models.CharField(max_length=10)
      imgprofile = models.ImageField(upload_to ='employee',null=True,default ='none/no-img.jpg')
      imgstraight = models.ImageField(upload_to ='employee',null=True,default ='none/no-img.jpg')
      imgtop = models.ImageField(upload_to ='employee',null=True,default ='none/no-img.jpg')
      imgbottom = models.ImageField(upload_to ='employee',null=True,default ='none/no-img.jpg')
      imgleft = models.ImageField(upload_to ='employee',null=True,default ='none/no-img.jpg')
      imgright = models.ImageField(upload_to ='employee',null=True,default ='none/no-img.jpg')
      
      def __str__(self):
        return self.employee_idd
    
      def get_url(self):
        return reverse('employee_detail',args=[self.status.slug,self.slug])

class Clocking(models.Model):
        employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
        door = models.CharField(max_length=5)
        temp = models.FloatField()
        date = models.DateField()
        time = models.TimeField()
        datetime = models.DateTimeField()
        
        def __str__(self):
            return self.door
        
        def get_url(self):
            return reverse('employee_Table',args=[self.employee_id.slug])

class Image_Clocking(models.Model):
	model_pic = models.ImageField(upload_to ='clocking',null=True,default ='none/no-img.jpg')
	