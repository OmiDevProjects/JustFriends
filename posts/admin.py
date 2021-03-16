from django.contrib import admin
from .models import Post, Thought, All_Post

admin.site.register(Post)
admin.site.register(Thought)
admin.site.register(All_Post)