from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from network.forms import LoginForm

def log_in(request):
    error= False
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect('/')
            else:
                error = True
    else :
        form = LoginForm()
        
    return render(request, 'login.html', locals())
    
def log_out(request):
    logout(request)
    return redirect('/') 

from django.contrib.auth.decorators import login_required

@login_required
def profil(request):
    return render(request, 'profil.html', locals())
