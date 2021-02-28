from django import forms 
from .models import Profile

class UpdateProfileImage(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']