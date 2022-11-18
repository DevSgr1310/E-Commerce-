from django.http.response import HttpResponse
from django.shortcuts import render
from SubAppp.models import Contact

# Create your views here.
def home(request):
    return render(request,'index.html')
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        msg=request.POST['msg']
        obj=Contact(name=name,email=email,subject=subject,msg=msg)
        obj.save()
    return render(request,'contact.html')