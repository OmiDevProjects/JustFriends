from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.core import serializers
import json

from .models import Post
from profiles.models import Profile
from .forms import PostForm

# Homepage View Function
def index(request):

    # Profile Info [ Logged in User ]
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = ''
    all_posts = Post.objects.all().order_by('-created')

    Post_form = PostForm(request.POST or None, request.FILES or None)

    data = {}

    if request.is_ajax():
        pic_id = json.loads(request.POST.get('id'))
        action = request.POST.get('action')

        if pic_id is None:
            if Post_form.is_valid():
                obj = Post_form.save(commit=False)
        else:
            obj = Post.objects.get(id=pic_id)

        obj.action = action
        obj.save()

        data = serializers.serialize('json', [obj,])
        return JsonResponse({'data': data})

    context = {}
    context['home'] = 'JustFriends Homepage'
    context['posts'] = all_posts
    context['profile'] = profile
    context['post_form'] = Post_form
    return render(request, 'posts/index.html', context)

def post_json_response(request):
    query_set = Post.objects.all()
    data = serializers.serialize('json', query_set)
    return JsonResponse({'data': data})