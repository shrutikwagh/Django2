from django.shortcuts import render,redirect
from .models import Emp,singer,song
from .form import EmpForm,EmpForm2,singerform,songform
def home(request):
    return render(request,'home.html')
def add_emp(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get("email")
        age=request.POST.get("age")
        contact=request.POST.get("contact")
        address=request.POST.get("address")
        print('------------------>',name,email,age,contact,address)
        e=Emp()
        e.name=name
        e.email=email
        e.contact=contact
        e.age=age
        e.address=address
        e.save()
        return redirect("/")
    else:
        return render(request,'addemp.html')
from .form import EmpForm,EmpForm2
    
def add_emp2(request):
        if request.method=="POST":
            f=EmpForm(request.POST)
            f.save()
            return redirect("/")
        else:
            f=EmpForm
            d={'form':f}
            return render(request,'addemp2.html',d)
def add_emp3(request):
        if request.method=="POST":
            f=EmpForm2(request.POST)
            f.save()
            return redirect("/")
        else:
            f=EmpForm2
            d={'form':f}
            return render(request,'form.html',d)

from .models import Emp
def emp_list(request):
    elist=Emp.objects.all()
    d={"el":elist}
    return render(request,"emplist.html")

def addsinger(request):
    if request.method=='POST':
        f=singerform(request.POST)
        f.save()
        return redirect("/")
    else:
        f=singerform()
        context={'form':f}
        return render(request,"form.html",context)

def addsong(request):
    if request.method=='POST':
        f=songform(request.POST)
        f.save()
        return redirect("/")
    else:
        f=songform()
        context={'form':f}
        return render(request,"form.html",context)
from .form import User,userform1,userform2
def adduser1(request):
    if request.method=='POST':
        f=userform1(request.POST)
        f.save()
        return redirect('/')
    else:
        f=userform1
        context={'form':f}
        return render(request,'form.html',context)
    
def adduser2(request):
    if request.method=='POST':
        f=userform2(request.POST)
        f.save()
        return redirect('/')
    else:
        f=userform2
        context={'form':f}
        return render(request,'form.html',context)