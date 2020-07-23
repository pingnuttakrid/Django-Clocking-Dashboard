from django.conf.urls import include, url
from faceweb import views

urlpatterns = [
    url(r'^(?P<id>[\w-]+)/edit/$', views.ClockingCreateAPIView.as_view()),
    url(r'^upload/$', views.ImageCreateAPIView.as_view()),
]
