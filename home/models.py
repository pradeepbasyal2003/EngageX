from django.db import models
from django.contrib.auth.models import User
from .ytapi import *
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    username = models.CharField(max_length=200 , blank = True )

    description = models.TextField()

    profile_img = models.ImageField(upload_to="media/" , blank= True)

    channel_id = models.CharField(max_length = 500)

    email = models.EmailField(blank = True)

    

    def save(self , *args , **kwargs):
        if self.username == "":
            self.username = self.user.username

        super().save(*args , **kwargs)


    subscriber = get_subscriber_count('UC0bG20RykiBFmCBqabR_5pg')

    def __str__(self):
        return self.username




