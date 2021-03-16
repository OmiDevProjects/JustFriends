from django.db import models
from django.contrib.auth.models import User

from posts.utils import get_filtered_image

from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

from itertools import chain
import random

ACTION_CHOICES= (
    ('NO_FILTER', 'no filter'),
    ('COLORIZED', 'colorized'),
    ('GRAYSCALE', 'grayscale'),
    ('BLURRED', 'blurred'),
    ('BINARY', 'binary'),
    ('INVERT', 'invert'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, default='avatar.png')
    background = models.ImageField(upload_to='backgrounds', blank=True, default='background.png')
    following = models.ManyToManyField(User, related_name='following', blank=True)
    bio = models.TextField(blank=True, default='No Bio')
    profession = models.CharField(blank=True, default='Student', max_length=255)
    dob_date = models.DateField(blank=True, null=True)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES, null=True)
    # is_online = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

    def my_posts(self):
        return self.post_set.all().order_by('-created')

    @property
    def num_posts(self):
        return self.post_set.all().count()

    @property
    def get_following(self):
        return self.following.all()

    def get_following_users(self):
        following = [user for user in self.get_following]
        return following

    @property
    def following_count(self):
        return self.following.all().count()

    def get_my_and_following_posts(self):
        users = [user for user in self.get_following]
        posts = []
        query_set = None

        for user in users:
            profile = Profile.objects.get(user=user)
            profile_posts = profile.post_set.all().order_by('-created')
            posts.append(profile_posts)

        my_posts = self.post_set.all()
        posts.append(my_posts)

        if len(posts) > 0:
            query_set = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
        
        return query_set

    def proposals_for_following(self):
        profiles = Profile.objects.all().exclude(user=self.user)
        following_list = [profile for profile in self.get_following]

        avaliable_list = [profile for profile in profiles if profile.user not in following_list]
        random.shuffle(avaliable_list)
        return avaliable_list[:3]

    def get_followers(self):
        query_set = Profile.objects.all()
        followers_list= []

        for profile in query_set:
            if self.user in profile.get_following:
                followers_list.append(profile)

        return followers_list

    @property
    def followers_count(self):
        return len(self.get_followers())

    @property
    def get_friends(self):
        friend_count = 0
        get_followings = self.get_following_users()
        get_followers = self.get_followers()

        for pro_follower in get_followers:
            if self.user in pro_follower.get_following:
                friend_count += 1

        return friend_count

    def get_friends_list(self):
        friends_list = []
        users = [user for user in self.get_following]

        for user in users:
            profile = Profile.objects.get(user=user)
            friends_list.append(profile)

        return friends_list

    def save(self, *args, **kwargs):
        
        # open image
        pil_img = Image.open(self.avatar)

        # convert the image to array and do some processing
        cv_img = np.array(pil_img)
        img = get_filtered_image(cv_img, self.action)

        # convert back to pil image
        im_pil = Image.fromarray(img)

        # save
        buffer = BytesIO()
        im_pil.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.avatar.save(str(self.avatar), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)