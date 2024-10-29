from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from home.models import Contact 
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render
from .models import Project  


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")

def contact_view(request):  
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        submit = request.POST.get("submit")
        contact = Contact(name=name, email=email, submit=submit, date=datetime.today())
        contact.save()
        messages.success(request, "Your message was successfully submitted!")
    
    return render(request, "contact.html")
def about(request):

    
    return render(request,"about.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/project")
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    
    return render(request, "login.html")


def project(request):
    projects = Project.objects.all()  
    return render(request, "project.html", {'projects': projects})  

def log_out(request):
    logout(request)
    return redirect("/login")
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})  






