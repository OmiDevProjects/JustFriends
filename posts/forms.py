from django import forms
from .models import Post, Thought

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_document', 'description']
        labels ={
            'post_document': ''
        }

class PostThought(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['thought']
        labels = {
            'thought': ''
        }

class VideoPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_document', 'description']
        labels = {
            'post_document': 'Video',
        }