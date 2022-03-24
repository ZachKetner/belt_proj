from django.shortcuts import render, redirect, HttpResponse
from .models import *
import bcrypt
from django.contrib import messages

# Create your views here.
def registration(request):
    return render(request, 'registration.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/')
        else:
            print(request.POST['password'])
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            print(pw_hash)
            newUser = User.objects.create(fName = request.POST['fName'],
            lName = request.POST['lName'], email = request.POST['email'], password = pw_hash)
            print(newUser.lName)
            messages.success(request, "Created a New User, please log in")
            return redirect('/')

    
def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/')
        else:
            loggedUser = User.objects.get(email = request.POST['email']) 
            request.session['user'] = loggedUser.id
            return redirect('/quotes')

def log_out(request):
    request.session.flush()
    return redirect('/')

