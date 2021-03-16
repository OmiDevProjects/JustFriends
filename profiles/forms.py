from django import forms 
from .models import Profile

from posts.utils import get_filtered_image

from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

class UpdateProfileImage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

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

class UpdateCoverImage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['background']