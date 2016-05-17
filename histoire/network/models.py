from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#specifications for Users

class Profil(models.Model): #use the post_save signal to create automatically
    user = models.OneToOneField(User)
    
    def __str__(self):
        return self.user.username



