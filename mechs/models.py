from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=49)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    profile_picture = models.ImageField(upload_to='images/',default="default.png")
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    location = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return f'{self.user.username} Customer'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

class Mechanics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mechanics')
    profile_picture = models.ImageField(upload_to='images/',default="default.png")
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    age=models.IntegerField()
    experience = models.IntegerField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE, related_name='mechanics')
    rating=models.FloatField()

    def __str__(self):
        return f'{self.user.username} Mechanics'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Mechanics.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.name} comment'




