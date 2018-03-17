from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField

# Create your models here.
class Neighborhood(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    neighborhood_name = models.CharField(max_length=30, blank=True)
    neighborhood_location = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.neighborhood_name

    def save_neighborhood(self):
        self.save()

    @classmethod
    def this_neighborhood(cls):
        area = cls.objects.objects.get(pk=this_object_id)
        return area


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="posts/",blank = True, null = True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    @classmethod
    def this_profile(cls):
        profile = cls.objects.objects.get(pk=this_object_id)
        return profile

class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=30, blank=True)
    post = HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)

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

def Create_neighborhood(sender, **kwargs):
    if kwargs['created']:
        user_neighborhood = Neighborhood.objects.create(user=kwargs['instance'])

post_save.connect(Create_neighborhood,sender=User)
