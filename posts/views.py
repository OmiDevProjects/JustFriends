from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.core import serializers
import json

from .models import Post, Thought, All_Post
from profiles.models import Profile
from .forms import PostForm, PostThought, VideoPostForm

# Homepage View Function
def index(request):

    # Profile Info [ Logged in User ]
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = ''
    all_posts = All_Post.objects.all().order_by('-created')

    Post_form = PostForm(request.POST or None, request.FILES or None)
    post_thought_form = PostThought(request.POST or None)
    videoForm = VideoPostForm(request.POST or None)

    data = {}

    # Ajax Request 
    if request.is_ajax():
        pic_id = json.loads(request.POST.get('id'))
        action = request.POST.get('action')
        author_profile = Profile.objects.get(user=request.user)

        if pic_id is None:
            if Post_form.is_valid():
                obj = Post_form.save(commit=False)
        else:
            obj = Post.objects.get(id=pic_id)

        obj.action = action
        obj.author = author_profile
        obj.save()

        all_feeds = All_Post(post=obj)
        all_feeds.save()

        data = serializers.serialize('json', [obj,])
        return JsonResponse({'data': data})

    if request.method == 'POST':
        thought = request.POST.get('thought')
        request_user = request.user
        profile_user = Profile.objects.get(user=request_user)

        thought_post = Thought()
        thought_post.thought = thought
        thought_post.author = profile_user
        thought_post.save()

        all_feeds = All_Post(thoughts=thought_post)
        all_feeds.save()

        return redirect('posts:homepage')

    # JSON  
    context = {
        'home': 'JustFriends Homepage',
        'allposts': all_posts,
        'profile': profile,
        'post_form': Post_form,
        'post_thought_form': post_thought_form,
        'videoForm': videoForm
    }
    return render(request, 'posts/index.html', context)

def post_json_response(request):
    query_set = Post.objects.all()
    data = serializers.serialize('json', query_set)
    return JsonResponse({'data': data})