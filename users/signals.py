from django.db.models.signals import post_save, post_delete
from users.models import Profile
from django.contrib.auth.models import User


# signals


# every a user is created or updated on the user model, then we make the changes on the profile model too
# @receiver(post_save, sender = Profile)
def createProfile(sender, instance, created, **kwargs):
    if (created):
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
    else:
        print("profile updated")


# @receiver(post_delete,sender = Profile)

def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


# this runs when a new profile is created or updated
def updatingProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if (not created):
        user.first_name = profile.name or " "
        user.username = profile.username
        user.email = profile.email
        user.save()


# updating profile -> which also updates the user model
post_save.connect(updatingProfile, sender=Profile)
post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
