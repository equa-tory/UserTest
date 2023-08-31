from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):

    GENDER = {
        ('male', 'Male'),
        ('female', 'Female')
    }
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to="img/avatar/",blank=True,null=True,verbose_name="Avatar")
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER)

    def __str__(self):
        return self.username
