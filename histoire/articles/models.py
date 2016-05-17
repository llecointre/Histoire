from django.db import models
from network.models import Profil

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    category = models.ForeignKey('Category')
    #mini_url = models.
    subcategories = models.CharField(null=True, max_length=100)
    contents = models.TextField(null=False) #possibilité de mettre ceci dans les thèmes et séparer par des grandes sections ???, ou telecharger un texte ???
    nb_views = models.IntegerField(default=0)
    author = models.ForeignKey('network.Profil') #maybe pass to ManyToMany after
    
    def __str__(self):
        return self.title
        
    #maybe add some permissions

class Category(models.Model):
    name = models.CharField(max_length=30)
     
    def __str__(self):
        return self.name
        
class Period(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
