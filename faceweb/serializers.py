from rest_framework import serializers

from rest_framework.serializers import (
      ModelSerializer,
)

from faceweb.models import Clocking,Image_Clocking


class ClockingSerializer(ModelSerializer):

   class Meta:
      model = Clocking
      fields = [
         'ref_id',
         'employee_id',
         'door',
         'temp',
         'date',
         'time',
	     'datetime'
         ]

class imageSerializer(ModelSerializer):

   model_pic = serializers.ImageField(max_length=None,use_url=True)   

   class Meta:
      model = Image_Clocking
      fields = [
         'model_pic'        
      ]