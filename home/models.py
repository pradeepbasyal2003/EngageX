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

    youtube_link = models.CharField(blank = True , max_length = 200)

    instagram_link = models.CharField(blank = True , max_length = 200)

    twitter_link = models.CharField(blank = True , max_length = 200)

    facebook_link = models.CharField(blank = True , max_length = 200)

    

    def save(self , *args , **kwargs):
        if self.username == "":
            self.username = self.user.username

        super().save(*args , **kwargs)

    channel_id="UCX6OQ3DkcsbYNE6H8uQQuVA"
    subscriber = get_subscriber_count(channel_id)
    reach = get_views_count(channel_id)
    videos = get_video_count(channel_id)
    def __str__(self):
        return self.username




