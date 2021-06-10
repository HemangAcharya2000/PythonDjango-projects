from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from  . models import student

def homepageview(request):
    return render(request,'home.html')


def aboutpageview(request):
    return render(request,'about.html')

def contactpageview(request):
    return render(request,'contect.html')

def myform(request):
    return render(request,'myform.html')

def process(request):
    print(request.method)
    print(request.POST)
    a= (request.POST['email'])
    b=(request.POST['psw'])
    c=(request.POST['psw-repeat'])

    
    return render(request,'ans.html',{'Email':a,'Password':b,'repeat':c})    


class studentlist(ListView):
    model = student
    template_name = 'slist.html'
    