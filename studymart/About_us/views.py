from django.shortcuts import render
from django.http import HttpResponse
from About_us.models import Teacher

# Create your views here.
def about_us(request):
          return render (request, 'about/about.html')


def teacher_info(request):
          teach=Teacher.objects.all() 
          return render (request,'about/t.html',{'thr':teach}) 