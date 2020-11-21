from django.shortcuts import render
from django.http import HttpResponse
from .models import DataIn

def home(request):
    form = DataIn()
    return render(request,'talkapp/home.html',{'form':form})
