from django.urls import path
from . import views

urlpatterns=[
   
    path('b/',views.blogs1,name='blog'),
    path('f/',views.showformsdata),

]