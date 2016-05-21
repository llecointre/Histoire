from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime

from articles.models import GeneralArticle, Character, Invention, Battle

def home(request):
    articles = GeneralArticle.objects.all()
    characters = Character.objects.all()
    inventions = Invention.objects.all()
    battles = Battle.objects.all()
    
    return render(request, 'base.html', {'last_articles':articles, 'characters':characters, 'inventions':inventions, 'battles':battles})
    

