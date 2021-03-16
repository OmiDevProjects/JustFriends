from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver

from .models import Profile

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(user_logged_in)
# def online(sender, user, request, **kwargs):
#     user.profile.is_online = True
#     user.profile.save()

# @receiver(user_logged_out)
# def offline(sender, user, request, **kwargs):
#     user.profile.is_online = False
#     user.profile.save()