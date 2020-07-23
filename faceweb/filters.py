from faceweb.models import Clocking
import django_filters 
from django_filters import NumberFilter,DateFilter


class ClockingFilter(django_filters.FilterSet):    
    temp_min = NumberFilter(field_name="temp",lookup_expr='gte')
    start_date = DateFilter(field_name="date", lookup_expr='gte')
    end_date = DateFilter(field_name="date", lookup_expr='lte')
    start_time = DateFilter(field_name="time", lookup_expr='gte')
    
    class Meta:
        model = Clocking
        fields = '__all__'


   