from django.urls import path
from . import views

urlpatterns=[
   
    path('dt/',views.data_analysis,name='data'),
    path('class/',views.DataAnalysis.as_view())


]