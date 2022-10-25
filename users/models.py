from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
# profiles -> each account will have only one profile page -> hence 1 -> 1 relationship

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=200, blank=True, null=True)

    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    email = models.EmailField(max_length=500, blank=True, null=True)

    short_intro = models.CharField(max_length=200, blank=True, null=True)

    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        blank=True, null=True, upload_to='profiles/', default="profiles/user-default.png")

    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    social_stackoverflow = models.CharField(
        max_length=200, blank=True, null=True)
    # social_instagram = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


# # signals
# # @receiver(post_save, sender = Profile)
# 
# # every a user is created or updated on the user model, then we make the changes on the profile model too
# def createProfile(sender, instance, created, **kwargs):
#     if (created):
#         user = instance
#         profile = Profile.objects.create(
#             user=user,
#             username=user.username,
#             email=user.email,
#             name=user.first_name,
#         )
#     else:
#         pass
# 
# # @receiver(post_delete,sender = Profile)
# 
# 
# def deleteUser(sender, instance, **kwargs):
#     # instance have access to the deleting object
#     user = instance.user
#     print(f"deleting user {user.username}")
#     user.delete()
# 
# 
# post_save.connect(createProfile, sender=User)
# post_delete.connect(deleteUser, sender=Profile)
