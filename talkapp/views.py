from django.shortcuts import redirect, render , HttpResponse
from random import choice
from .models import DataIn
from .phone import to_phoneme
from django.contrib import messages

def home(request):
    list_homo = []
    with open('datasets/homophones.txt','r') as hom_file:
        line = hom_file.readline()
        while line:
            list_homo.append(line.split(','))
            line = hom_file.readline() 
    if(request.method == 'POST'):
        message = request.POST['message']
        to_phoneme(message)
        list_homo_ = []
        with open('datasets/phoneme.txt') as ph:
            line = ph.readline()
            while line:
                list_homo_.append(line)
                line = ph.readline() 
        return render(request,'talkapp/phoneme.html',{'data':list_homo_})
    form = DataIn()
    return render(request,'talkapp/home.html',{'form':form,'homophones':choice(list_homo)})
