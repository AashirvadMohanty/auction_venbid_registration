from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    companyname = models.CharField(max_length=40, blank=True)
    mobileno = models.CharField(max_length=15, blank=True)
    telephone = models.CharField(max_length=15, blank=True)#models.DateField(null=True, blank=True)
    addresslane1 = models.TextField(max_length=100, blank=True)
    addresslane2 = models.TextField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    postalzip = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=15, blank=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()