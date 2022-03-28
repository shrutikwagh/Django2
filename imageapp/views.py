from multiprocessing import context
from django.shortcuts import redirect, render
from .models import imageform,imagemodel
def addimage(request):
    if request.method=='POST':
        f=imageform(request.POST,request.FILES)
        f.save()
        imgl=imagemodel.objects.all()
        context={'form':f,'imgl':imgl}
        return render(request,'image.html',context)
    else:
        f=imageform
        context={'form':f}
        return render(request,'image.html',context)
    
def msg_data(request):
    if request.method=='POST':
        pass
    else:
        lmsg="this is login form"
        context={'fmsg':"This is First Message given by render"}
        return render(request,"msg.html",context)