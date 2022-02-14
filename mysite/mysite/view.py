from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from mysite.models import Index 

def index(request):
    if request.method=="POST":
        
        name=request.POST['name']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['phone']
        #print(fname,lname,email,phone)

        ins=Index(name=name,lname=lname,email=email,phone=phone)
        ins.save()
        print("Data has written")
    
    return render(request,'index.html')




