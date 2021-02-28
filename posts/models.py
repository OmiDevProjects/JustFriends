from django.db import models
from django.contrib.auth.models import User
from .utils import get_filtered_image

from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

from profiles.models import Profile

ACTION_CHOICES= (
    ('NO_FILTER', 'no filter'),
    ('COLORIZED', 'colorized'),
    ('GRAYSCALE', 'grayscale'),
    ('BLURRED', 'blurred'),
    ('BINARY', 'binary'),
    ('INVERT', 'invert'),
)

class Post(models.Model):
    post_document = models.FileField(upload_to='Post_documents', blank=True, null=True, default='post.png')
    description = models.TextField(blank=True, null=True)
    liked = models.ManyToManyField(User, default=None, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES, null=True)
    #comment
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.description) + ' ' + str(self.pk)
    
    def get_liked(self):
        return self.liked.all()

    @property
    def like_count(self):
        return self.liked.all().count()

    def get_user_liked(self, user):
        pass

    def find_typecheck(self):
        filename = self.post_document.name
        try:
           ext = filename.split('.')[-1]
           if ext == 'jpg' or ext == 'png' or ext == 'jpeg':
              a=1
           else:
              a=2
        except Exception:
           a = -1 # couldn't determine
        return a

    def save(self, *args, **kwargs):
        
        # open image
        pil_img = Image.open(self.post_document)

        # convert the image to array and do some processing
        cv_img = np.array(pil_img)
        img = get_filtered_image(cv_img, self.action)

        # convert back to pil image
        im_pil = Image.fromarray(img)

        # save
        buffer = BytesIO()
        im_pil.save(buffer, format='png')
        image_png = buffer.getvalue()

        self.post_document.save(str(self.post_document), ContentFile(image_png), save=False)

        super().save(*args, **kwargs)