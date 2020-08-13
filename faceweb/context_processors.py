from faceweb.models import Status,Employee
from django.contrib.auth.models import User


def menu_links(request):
    links=Status.objects.all()
    return dict(links=links)

def user_links(request):
    user=User.objects.all().latest('last_login')
    email = user.email
    profile = Employee.objects.all().filter(email=email)[0]

    
    return dict(user_links=profile)