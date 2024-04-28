from django.db import models

# Create your models here.
class Banner(models.Model):
    image:models.ImageField(upload_to="images/")
    title:models.CharField(max_length=500)

class User(models.Model):
    name:models.CharField(max_length=50)
    title:models.CharField(max_length=500)

class NewsEvents(models.Model):
    image:models.ImageField(upload_to="images/")
    date:models.DateField()
    mode:models.TextChoices("mode", "Online Offline")
    venue:models.CharField(max_length=500)
    keynoteSpeaker:models.ForeignKey(User, on_delete=models.DO_NOTHING)
    proramCoordinator:models.ForeignKey(User, on_delete=models.DO_NOTHING)
    chairPerson:models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Gallery(models.Model):
    image:models.ImageField(upload_to="images/")

class Opportunities(models.Model):
    name:models.CharField(max_length=500)
    institute:models.CharField(max_length=500)
    email:models.EmailField(blank=True)
    phone:models.CharField(max_length=25, blank=True)