from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    username = models.CharField(max_length=200 , blank = True)

    description = models.TextField()

    profile_img = models.ImageField(upload_to="media" , blank= True)

    channel_id = models.CharField(max_length = 500)

    def save(self , *args , **kwargs):
        if self.username == "":
            self.username = self.user.username

        super().save(*args , **kwargs)


    def __str__(self):
        return self.username



