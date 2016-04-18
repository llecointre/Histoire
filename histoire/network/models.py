from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    category = models.ForeignKey('Category')
    #mini_url = models.
    subcategories = models.CharField(null=True, max_length=100)
    contents = models.TextField(null=False) #possibilité de mettre ceci dans les thèmes et séparer par des grandes sections ???, ou telecharger un texte ???
    nb_views = models.IntegerField(default=0)
    author = models.ForeignKey('Profil') #maybe pass to ManyToMany after
    
    def __str__(self):
        return self.title
        
    #maybe add some permissions

class Category(models.Model):
    nom = models.CharField(max_length=30)
     
    def __str__(self):
        return self.nom
        
class Period(models.Model):
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom

class People(models.Model):
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom

class Character(models.Model):
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom

class Region(models.Model):
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom
                                                                                                          
        
#specifications for Users

class Profil(models.Model): #use the post_save signal to create automatically
    user = models.OneToOneField(User)
    
    def __str__(self):
        return self.user.username



