from django.shortcuts import render, redirect
from .models import Profile
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from .forms import UpdateProfileImage, UpdateCoverImage

from django.core import serializers
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm, userLoginForm

def user_register_form(request):

    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}! Your Account is Created. You can login now')
            form.save()
            return redirect('profiles:user_login')

    context = {
        'form': form,
    }
    return render(request, 'users_app/signup.html', context)

def user_login_form(request):

    form = userLoginForm()

    if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('')
        form = userLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticating
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('posts:homepage')

    context = {
        'form': form,
    }
    return render(request, 'users_app/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('profiles:user_login')

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