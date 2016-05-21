from django.db import models
from network.models import Profil

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    #mini_url = models.
    content = models.TextField(null=False) #possibilité de mettre ceci dans les thèmes et séparer par des grandes sections ???, ou telecharger un texte ???
    nb_views = models.IntegerField(default=0)
    author = models.ManyToManyField('network.Profil') #maybe pass to ManyToMany after
    
    class Meta:
        abstract = True
        
class GeneralArticle(Article):
    
    def __str__(self):
        return self.title        


####### PERIOD ######

class PeriodArticle(Article):
    period = models.ForeignKey('Period')
    
    def __str__(self):
        return self.title
        
class Period(models.Model): #epoque, dynastie...
    name = models.CharField(max_length=50)
     
    
    def __str__(self):
        return self.name

####### PEOPLE #######

class PeopleArticle(Article):
    people = models.ForeignKey('People')
    
    def __str__(self):
        return self.title
        
class People(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
####### ART ########

class ArtArticle(Article):
    art = models.ForeignKey('Art')
    
    def __str__(self):
        return self.title
        
class Art(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        

######## PHILOSOPHY #######

class PhilosophyArticle(Article):
    philosophy = models.ForeignKey('Philosophy')
    
    def __str__(self):
        return self.title
        
class Philosophy(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


####### RELIGION ########

class ReligionArticle(Article):
    religion = models.ForeignKey('Religion')
    
    def __str__(self):
        return self.title
        
class Religion(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name     

####### CHARACTER #######

class CharacterArticle(Article):
    character = models.ForeignKey('Character')
    
    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    latitude = models.FloatField(null=True) #add validators
    longitude = models.FloatField(null=True)
    
    def __str__(self):
        return self.name
    

###### REGION #######

class RegionArticle(Article):
    region = models.ForeignKey('Region')
    
    def __str__(self):
        return self.title

class Region(models.Model): #avec plusieurs niveaux qui vont correspondre a leur zoom d'apparition 
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
        
######## EVENT ########

class EventArticle(Article):

    class Meta:
        abstract = True 
        
class InventionArticle(EventArticle):
    invention = models.ForeignKey('Invention')
    ## + possibilite d'ajouter un inventeur relie a la classe personnage
    
    def __str__(self):
        return self.title
        
class Invention(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    latitude = models.FloatField(null=True) #add validators
    longitude = models.FloatField(null=True)
    
    def __str__(self):
        return self.name
        
class WarArticle(EventArticle):
    invention = models.ForeignKey('Invention')
    ## + possibilite d'ajouter un inventeur relie a la classe personnage
    
    def __str__(self):
        return self.title
        
class War(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class BattleArticle(EventArticle):
    battle = models.ForeignKey('Battle')
    
    def __str__(self):
        return self.title
        
class Battle(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    war = models.ForeignKey('War')
    latitude = models.FloatField(null=True) #add validators
    longitude = models.FloatField(null=True)
    description = models.TextField(null=False)
    
    def __str__(self):
        return self.name
    
