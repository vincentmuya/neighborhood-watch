from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField

# Create your models here.
class Neighborhood(models.Model):
    neighborhood_location = models.CharField(max_length=30, blank=True)


    def __str__(self):
        return self.neighborhood_location

    def save_neighborhood(self):
        self.save()

    @classmethod
    def this_neighborhood(cls):
        area = cls.objects.all()
        return area


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="posts/",blank = True, null = True)
    bio = models.TextField(max_length=500, blank=True)
    Neighborhood = models.ForeignKey(Neighborhood,null = True)
    neighborhood_name = models.CharField(max_length=30, blank=True)


    def save_profile(self):
        self.save()

    @classmethod
    def this_profile(cls):
        profile = cls.objects.all()
        return profile

class Post(models.Model):
    user = models.ForeignKey(User, null = True)
    title = models.CharField(max_length=30, blank=True)
    post = HTMLField()

    def __str__(self):
        return self.title

    @classmethod
    def this_post(cls):
        posts = cls.objects.all()
        return posts


def Create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(Create_profile,sender=User)
