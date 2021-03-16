from django.shortcuts import render, redirect
from .models import Profile
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from .forms import UpdateProfileImage, UpdateCoverImage

from django.core import serializers
import json

def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    update_avatar_form = UpdateProfileImage(request.FILES or None)
    update_cover_image = UpdateCoverImage(request.FILES or None)

    context = {
        'form_avatar': update_avatar_form,
        'cover_image_form': update_cover_image,
        'profile': profile,
    }
    return render(request, 'profiles/profile.html', context)

def get_profile(request, *args, **kwargs):
    profile = Profile.objects.get(user=kwargs.get('profile_id'))
    context = {}
    context['profile'] = profile
    return render(request, 'profiles/profile.html', context)

def update_profile_image(request):
    
    data = {}

    if request.is_ajax():
        pic_id = json.loads(request.POST.get('id'))
        action = request.POST.get('action')
        image = request.FILES.get('avatar')

        if pic_id is None:
            obj = Profile.objects.get(user=request.user)
        else:
            obj = Profile.objects.get(id=pic_id)

        obj.action = action
        obj.avatar = image
        obj.save()

    data = serializers.serialize('json', [obj,])
    return JsonResponse({'data': data})

def update_cover_image(request):
    
    data = {}

    if request.is_ajax():
        pic_id = json.loads(request.POST.get('id_cover'))
        image = request.FILES.get('cover')

        if pic_id is None:
            obj = Profile.objects.get(user=request.user)
            print('If :', obj)
        else:
            obj = Profile.objects.get(id=pic_id)
            print('Else : ', obj)

        obj.background = image
        obj.save()

    data = serializers.serialize('json', [obj,])
    return JsonResponse({'cover': data})