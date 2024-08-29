from django.db import models
from django.contrib.auth.models import User
from .ytapi import *
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    username = models.CharField(max_length=200 , blank = True )

    description = models.TextField()

    profile_img = models.ImageField(upload_to="media/" , blank= True)

    channel_id = models.CharField(max_length = 500 , blank=True)

    email = models.EmailField(blank = True)

    youtube_link = models.CharField(blank = True , max_length = 200)

    instagram_link = models.CharField(blank = True , max_length = 200)

    twitter_link = models.CharField(blank = True , max_length = 200)

    facebook_link = models.CharField(blank = True , max_length = 200)

    

    # channel_id="UCX6OQ3DkcsbYNE6H8uQQuVA"
    def subscriber(self):
        if self.channel_id:
            return get_subscriber_count(self.channel_id)
        return None

    @property
    def reach(self):
        if self.channel_id:
            return get_views_count(self.channel_id)
        return None

    @property
    def videos(self):
        if self.channel_id:
            return get_video_count(self.channel_id)
        return None
    
    def save(self , *args , **kwargs):
        if self.username == "":
            self.username = self.user.username

        super().save(*args , **kwargs)
    def __str__(self):
        return self.username




