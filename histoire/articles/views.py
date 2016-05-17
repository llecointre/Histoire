from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime

from articles.models import Article

# Create your views here.

def read(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'read.html', {'article':article})
