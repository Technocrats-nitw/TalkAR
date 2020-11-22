from django.shortcuts import redirect, render , HttpResponse
from random import choice
from .models import DataIn
from .phone import to_phoneme
import mimetypes 


def home(request):
    list_homo = []
    with open('datasets/homophones.txt','r') as hom_file:
        line = hom_file.readline()
        while line:
            list_homo.append(line.split(','))
            line = hom_file.readline()        
    form = DataIn()
    return render(request,'talkapp/home.html',{'form':form,'homophones':choice(list_homo)})

def file_download(request):
    if(request.method == 'POST'):
        message = request.POST['message']
        to_phoneme(message)
        with open('datasets/phoneme.txt') as phon:
            data = phon.read()
        return HttpResponse(data)
    else:
        with open('datasets/phoneme.txt') as phon:
            data = phon.read()
        return HttpResponse(data)
    





        # fl_path = 'datasets/phoneme.txt'
        # filename = 'phoneme.txt'
        # fl = open(fl_path, 'r')
        # mime_type, _ = mimetypes.guess_type(fl_path)
        # response = HttpResponse(fl, content_type=mime_type)
        # response['Content-Disposition'] = "attachment; filename=%s" % filename
        # return response