import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    headline = models.CharField(max_length=500, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    location = models.ImageField(blank=True, null=True, upload_to='profiles/', default='profiles/user-default.png')
    profile_image = models.CharField(max_length=200, blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    objects = models.Manager()

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    objects = models.Manager()

    def __str__(self):
        return str(self.name)


def create_profle(sender, instance, created, **kwargs):
    if created:
        user = instance
        Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
            )
post_save.connect(create_profle, sender=User)


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_delete.connect(delete_user, sender=Profile)
