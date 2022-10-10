from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def deep_learning(request):
          return render (request,'deep_learning/deep_learning.html')

def registration(request):
          if request.method =="POST":
                    fmm = UserCreationForm(request.POST)
           
                    if fmm.is_valid():
                              fmm.save()                
          else:
           fmm= UserCreationForm()
          return render (request,'deep_learning/register.html',{'form':fmm})    
