from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# Create your models here.
from cloudinary.models import CloudinaryField

class Location(models.Model):
    location = models.CharField(max_length=45,blank=True)

    def __str__(self):
        return f'{self.location} '
class Rating(models.Model):
    rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='rater')
    communication = models.IntegerField(choices=rating, default=0, blank=True)
    punctuality = models.IntegerField(choices=rating, blank=True)
    workrate = models.IntegerField(choices=rating, blank=True)
    score = models.FloatField(default=0, blank=True)
    communiaction_average = models.FloatField(default=0, blank=True)
    punctuality_average = models.FloatField(default=0, blank=True)
    workrate_average = models.FloatField(default=0, blank=True)

    def __str__(self):
        return f'{self.score} Rating'

class Mechanic(models.Model):
    name = models.CharField(max_length=80, blank=True)
    profile_picture = models.ImageField(upload_to="pictures/",default="default.jpg")
    age = models.IntegerField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    ratings = models.ForeignKey(Rating,on_delete=models.SET_NULL, null=True,related_name ="mechanic")

    # call
    def __str__(self):
        return f'{self.name} '

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
