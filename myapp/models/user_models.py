from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

class Customer(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    membership_level = models.CharField(max_length=50)
