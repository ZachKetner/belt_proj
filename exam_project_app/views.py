from django.shortcuts import render, redirect, HttpResponse
from .models import *
from login_and_reg_app.models import *
import bcrypt
from django.contrib import messages
from .forms import QuoteForm

def index(request):
    if 'user' not in request.session:
        return redirect('/')
    selectedUser = User.objects.get(id=request.session['user'])
    context = {
        'All_quotes': Quotes.objects.all(),
        'All_users': User.objects.all(),
        'user': selectedUser,
    }
    form = QuoteForm()
    return render(request, 'index.html', context, {"form":form})

def create(request):
    if request.method =='POST':
        errors = Quotes.objects.quote_validator(request.POST)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/quotes')
        else:
            newQuote = Quotes.objects.create(author = request.POST['author'], description = request.POST['description'],
            quoter = User.objects.get(id=request.session['user']))
            print(newQuote.author)
            print(newQuote.description)
            return redirect('/quotes')

def add_like(request, userid):
    liked_quote = Quotes.objects.get(id=userid)
    quote_liking = User.objects.get(id=request.session['user'])
    liked_quote.quote_likes.add(quote_liking)
    return redirect('/quotes')

def userQuotes(request, userid):
    if 'user' not in request.session:
        return redirect('/')
    else:
        context ={
            'user': User.objects.get(id=userid),
        }
        return render(request, 'userPage.html', context)

def userProfile(request, userid):
    if 'user' not in request.session:
        return redirect('/')
    else:
        context ={
            'user': User.objects.get(id=userid),
        }
        return render(request, 'profile.html', context)

def update(request, userid):
    if request.method =='POST':
        errors = User.objects.update_validator(request.POST)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect(f'/quotes/myaccount/{userid}')
        else:
            edit_user = User.objects.get(id=userid)
            edit_user.first_name = request.POST['fName']
            edit_user.last_name = request.POST['lName']
            edit_user.email = request.POST['email']
            edit_user.save()
            return redirect('/quotes')

def delete(request, userid):
    destroyQuote = Quotes.objects.get(id=userid)
    destroyQuote.delete()
    return redirect('/quotes')
# Create your views here.
