#from pyexpat import model
from django.db import models

from django.contrib.auth.models import AbstractUser

#Creamos modelo de usuario con AbstractUser
class User(AbstractUser):
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Customer(User): # necesidad de extender nuevas funcionalidades
    class Meta:
        proxy = True
    
    def get_products(self):
        return []

class Profile(models.Model): ## para generar nuevos atributos al modelo existente 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()