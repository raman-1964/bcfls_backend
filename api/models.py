from django.db import models

# Create your models here.
class Banner(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=500)
      
    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=500)
      
    def __str__(self):
        return self.name

class NewsEvents(models.Model):
    MODE_ONLINE = 'ONLINE'
    MODE_OFFLINE = 'OFFLINE'

    MODE_CHOICES = [
        (MODE_ONLINE, 'online'),
        (MODE_OFFLINE, 'offline'),
    ]
    
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    date = models.DateField()
    mode = models.CharField(
        max_length=7, choices=MODE_CHOICES, default=MODE_OFFLINE)
    venue = models.CharField(max_length=500)
    is_home_page = models.BooleanField(default=False)
    keynoteSpeaker = models.ManyToManyField(User, related_name='keynoteSpeaker', default=None, blank=True)
    chairPerson = models.ManyToManyField(User, related_name='chairPerson', default=None, blank=True)
    programCoordinator = models.ManyToManyField(User, related_name='programCoordinator_events', default=None, blank=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    image = models.ImageField(upload_to="images/")
    is_home_page = models.BooleanField(default=False)

class Opportunities(models.Model):
    name = models.CharField(max_length=500, blank=False)
    institute = models.CharField(max_length=500, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    phone = models.CharField(max_length=25, blank=False)