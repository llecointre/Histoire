from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime

from articles.models import Article

def home(request):
    articles = Article.objects.all()
    return render(request, 'base.html', {'last_articles':articles})
    

