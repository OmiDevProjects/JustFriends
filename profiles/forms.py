from django import forms 
from .models import Profile

from posts.utils import get_filtered_image

from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password ( Strong Password )', widget=forms.PasswordInput(attrs={'placeholder': 'Password ( Strong Password )'}))
    password2 = forms.CharField(label='Confirm Password',  widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class userLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Verifed Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your Password'}))

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

class UpdateProfileInfo(forms.Form):
    bio = forms.CharField(widget=forms.Textarea())
    # dob = forms.DateField(input_formats='%Y-%m-%d')
    profession = forms.CharField(max_length=255)
