from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from adminapp.models import petsdb, categorydb, servicedb, acceptdb
from userapp.models import requestdb
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def index(request):
    return render(request,'index.html')
def add_pets(request):
    data=categorydb.objects.all()
    return render(request,'pets.html',{'data':data})
def savepets(request):
    if request.method=="POST":
        p=request.POST.get('pets')
        b=request.POST.get('breed')
        i=request.FILES['image']
        pr=request.POST.get('price')
        dr=request.POST.get('description')
        obj=petsdb(pets=p,breed=b,image=i,rate=pr,description=dr)
        obj.save()
        return redirect(add_pets)
def display_pets(request):
    data=petsdb.objects.all()
    return render(request,"display.pets.html",{'data':data})
def delpets(req,id):
    data=petsdb.objects.filter(id=id)
    data.delete()
    return redirect(display_pets)
def editpets(request,id):
    data=petsdb.objects.get(id=id)
    return render(request,"edit.pets.html",{'data':data})


def update(request,id):
    if request.method=="POST":
        pe=request.POST.get('pets')
        br=request.POST.get('breed')
        ra=request.POST.get('rate')
        dr = request.POST.get('description')
        try:
            im=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=petsdb.objects.get(id=id).image
        petsdb.objects.filter(id=id).update(pets=pe,breed=br,rate=ra,image=file,description=dr)
        return redirect(display_pets)

def logg(request):
    return render(request,'log.html')
def log(request):
    if request.method=="POST":
        uname=request.POST.get("uname")
        pwd=request.POST.get("pwd")
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=uname
                request.session['password']=pwd
                messages.success(request,"LOGIN SUCCESSFULLY")
                return redirect(index)
            else:
                messages.error(request,"INVALID USERNAME OR PASSWORD")
                return redirect(logg)
        else:
            messages.error(request,"INVALID USERNAME OR PASSWORD")
            return redirect(logg)


def logout_pg(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "LOGOUT SUCCESSFULLY")
    return redirect(logg)

def category(request):
    return render(request,'category.html')
def savecategory(request):
    if request.method=="POST":
        n=request.POST.get('name')
        i=request.FILES['image']
        dr=request.POST.get('description')
        obj=categorydb(name=n,image=i,description=dr)
        obj.save()
        return redirect(category)
def display_category(request):
    data=categorydb.objects.all()
    return render(request,"display.category.html",{'data':data})
def delcategory(req,id):
    data=categorydb.objects.filter(id=id)
    data.delete()
    return redirect(display_category)
def addservice(req):
    return render(req,'add.service.html')
def saveservice(request):
    if request.method=="POST":
        n=request.POST.get('name')
        i=request.FILES['image']
        dr=request.POST.get('description')
        pr=request.POST.get('price')
        obj=servicedb(name=n,image=i,description=dr,price=pr)
        obj.save()
        return redirect(addservice)
def displayservice(req):
    data=servicedb.objects.all()
    return render(req,'display.service.html',{'data':data})
def editservice(request,id):
    data=servicedb.objects.get(id=id)
    return render(request,"edit.service.html",{'data':data})
def updateservice(request,id):
    if request.method=="POST":
        na=request.POST.get('name')
        dr=request.POST.get('description')
        pr=request.POST.get('price')
        try:
            im=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=servicedb.objects.get(id=id).image
        servicedb.objects.filter(id=id).update(name=na,description=dr,price=pr,image=file)
        return redirect(displayservice)
def delservice(req,id):
    data=servicedb.objects.filter(id=id)
    data.delete()
    return redirect(displayservice)
def displayadopt(request):
    data=requestdb.objects.all()
    return render(request,'display.adopt.html',{'data':data})
def deladopt(req,id):
    data=requestdb.objects.filter(id=id)
    data.delete()
    messages.success(req, "your request has been deleted")
    return redirect(displayadopt)
def saveaccept(req,id):
    if req.method=="POST":
        n=req.POST.get('name')
        m=req.POST.get('mobile')
        a=req.POST.get('address')
        b=req.POST.get('breed')
        obj=acceptdb(name=n,mobile=m,address=a,breed=b)
        obj.save()
    
    data=requestdb.objects.filter(id=id)
    data.delete()
    messages.success(req, "your request has been approved")
    return redirect(displayadopt)




