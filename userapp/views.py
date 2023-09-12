from django.contrib import messages
from django.shortcuts import render, redirect
from adminapp.models import petsdb, categorydb,servicedb
from userapp.models import contactdb, appoinmentdb, registerdb, requestdb
from django.contrib import messages


# Create your views here.
def home(request):
    data=categorydb.objects.all()
    return render(request,'home.html',{'data':data})
def dog(request,dogg):
    data=petsdb.objects.filter(pets=dogg)
    return render(request,'dog.html',{'data':data})
def cat(request,catt):
    data=categorydb.objects.filter(name=catt)
    return render(request,'cat.html',{'data':data})
def contact(request):

    return render(request,'contact.html')
def savecontact(request):
    if request.method=="POST":
        n=request.POST.get('name')
        e=request.POST.get('email')
        m=request.POST.get('mobile')
        ms=request.POST.get('message')
        obj=contactdb(name=n,email=e,mobile=m,message=ms)
        obj.save()
        messages.success(request, "Your message has send our team")
        return redirect(contact)
def details(request,dataid):
    data=petsdb.objects.filter(id=dataid)
    return render(request,'details.html',{'data':data})

def service(request):
    data=servicedb.objects.all()
    return render(request,'service.html',{'data':data})
def appoinment(request):
    return render(request,'appoinment.html')
def saveappoinment(request):
    if request.method=="POST":
        n=request.POST.get('name')
        e=request.POST.get('email')
        ph=request.POST.get('phone')
        pur=request.POST.get('purpose')
        dt=request.POST.get('date')
        obj=appoinmentdb(name=n,email=e,phone=ph,purpose=pur,date=dt)
        obj.save()
        messages.success(request,"your appointment has been submitted")
        return redirect(appoinment)
def about(request):
    return render(request,'about.html')
def register(req):
    return render(req,'register.html')
def saveregister(request):
    if request.method=="POST":
        n=request.POST.get('name')
        e=request.POST.get('email')
        ph=request.POST.get('phone')
        pss=request.POST.get('password')
        obj=registerdb(name=n,email=e,phone=ph,password=pss)
        obj.save()
        messages.success(request,"Register Successfully")
        return redirect(login)
def login(req):
    return render(req,'login.html')
def userlogin(req):
    if req.method=="POST":
        uname=req.POST.get('email')
        pswd=req.POST.get('password')
        if registerdb.objects.filter(email=uname,password=pswd).exists():
            req.session['email']=uname
            req.session['password']=pswd
            messages.success(req,"Login successfully")
            return redirect(home)
        else:
            messages.error(req, "Incorrect username or password")
            return redirect(login)
    else:
        messages.error(req,"Incorrect username or password")
        return redirect(login)
def logout(req):
    del req.session['email']
    del req.session['password']
    messages.success(req, "Logout Successfully")
    return redirect(login)
def request(req):
    return render(req,'reqst.html')
def saverequest(req):
    if req.method=="POST":
        n=req.POST.get('name')
        m=req.POST.get('mobile')
        a=req.POST.get('address')
        b=req.POST.get('breed')
        obj=requestdb(name=n,mobile=m,address=a,breed=b)
        obj.save()
        messages.success(req,"your request has been successfully submitted")
        return redirect(request)