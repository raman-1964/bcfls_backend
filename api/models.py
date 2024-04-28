from django.db import models

# Create your models here.
class Banner(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=500)

class User(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=500)

class NewsEvents(models.Model):
    MODE_ONLINE = 'ONLINE'
    MODE_OFFLINE = 'OFFLINE'

    MODE_CHOICES = [
        (MODE_ONLINE, 'online'),
        (MODE_OFFLINE, 'offline'),
    ]
    
    image = models.ImageField(upload_to="images/")
    date = models.DateField()
    mode = models.CharField(
        max_length=7, choices=MODE_CHOICES, default=MODE_OFFLINE)
    venue = models.CharField(max_length=500)
    keynoteSpeaker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='keynoteSpeaker')
    proramCoordinator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proramCoordinator')
    chairPerson = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chairPerson')

class Gallery(models.Model):
    image = models.ImageField(upload_to="images/")

class Opportunities(models.Model):
    name = models.CharField(max_length=500, blank=False)
    institute = models.CharField(max_length=500, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    phone = models.CharField(max_length=25, blank=False)