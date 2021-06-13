from django.shortcuts import redirect, render
from django.http import HttpResponse
from myapp.models import database
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request,'index.html')


def register(request):
    if request.method=='POST':
        username = request.POST['username']
        password1 = request.POST['psw']
        password2 = request.POST['psw-repeat']
        
        if password1==password2:
            
             if User.objects.filter(username=username).exists():
                   messages.warning(request, 'username alrady exists')
                   return redirect('register')
             else:
                 user = User.objects.create_user(username=username,password=password1)
                 user.save()
                 messages.success(request, 'your data has been sent')
                 return redirect('login')
                
        else:
            messages.warning(request, 'password not matching')  
        return redirect('register')
    else:
     return render(request,'register.html')  
    
        
     
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        contact = database(name=name,email=email,phone=phone,subject=subject)
        contact.save()
        messages.success(request, 'your message has been sent')
    return render(request,'contact.html')

def info(request):
    return render(request,'info.html')


def login(request):
    if request.method == "POST":
         username = request.POST['username']
         password = request.POST['psw']
        
         user = auth.authenticate(uaername=username, password=password)
        
         if user is not None:
            auth.login(request, user)
            return redirect('/')
         else:
             messages.warning(request, 'invalid input')
             return redirect('login')
             
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')