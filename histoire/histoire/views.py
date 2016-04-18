from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime

def home(request):
    return render(request, 'base.html', locals())
