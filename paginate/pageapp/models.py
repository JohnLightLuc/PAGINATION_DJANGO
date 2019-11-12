from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    tel = models.CharField(max_length=20)