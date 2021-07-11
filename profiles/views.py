from django.shortcuts import render, redirect
from .models import Profile, User_OTP

from django.views.generic import TemplateView, View
from django.http import JsonResponse
from .forms import UpdateProfileImage, UpdateCoverImage, UpdateProfileInfo

from django.core import serializers
import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm, userLoginForm

from django.conf import settings
from django.core.mail import send_mail
import random

def send_otp(user):
    
    user_otp = random.randint(100000, 999999)
    if User_OTP.objects.filter(user=user).exists():
        user_ = User_OTP.objects.filter(user=user).last()
        user_.otp = user_otp
        user_.save()
    else:
        User_OTP.objects.create(user=user, otp=user_otp)
    email = user.user.email
    message = f'Hello {user.user}, \n Your OTP is {user_otp}\n\nThankYou...'
    send_mail(
        'Hey, Welcome to JustFriends Platform - Verify Your Email',
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently = False
    )

def user_register_form(request):

    if not request.user.is_authenticated:
        form = UserRegisterForm()
        if request.method == 'POST':
            form = UserRegisterForm(request.POST or None)

            if form.is_valid():
                username = form.cleaned_data.get('username')
                messages.success(request, f'{username}! Your Account is Created. You can login now')
                instance = form.save()
                instance.is_active = False
                instance.save()

                try:
                    profile = Profile.objects.get(user=instance)
                except Exception as e:
                    profile = ''
                    print(e)

                send_otp(profile)
                request.session['user'] = username
                return redirect('profiles:otp_verification')

        context = {
            'form': form,
        }
        return render(request, 'users_app/signup.html', context)
    else:
        return redirect('homepage')

def otp_verification(request):

    if 'user' in request.session:
        user = request.session.get('user')
        user_obj = User.objects.get(username=user)
    else:
        messages.info(request, 'Please Create an Account')
        return redirect('profile:user_register')
    
    try:
        profile = Profile.objects.get(user=user_obj)
    except Exception as e:
        print(e)

    if request.method == 'POST':
        otp = request.POST.get('otp')

        if int(otp) == User_OTP.objects.filter(user = profile).last().otp:

            # Activate the Account
            user_obj.is_active = True
            user_obj.save()

            messages.success(request, f'{profile.user} Your Account is Created!!! Thanks For Registrations. Now you can login ')
            return redirect('profiles:user_login')
        else:
            messages.warning(request, 'Your OTP Does Not Match... Your Entered Wrong OTP!')
            return redirect('profiles:otp_verification')

    context = {}
    return render(request, 'users_app/otp_verify.html', context)

def user_login_form(request):

    if not request.user.is_authenticated:
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

                elif not User.objects.filter(username=username).exists():
                        messages.warning(request, 'User with this Username is Not Exist')
                        return redirect('profiles:user_login')

                elif not User.objects.get(username=username).is_active:
                        user_obj = User.objects.get(username=username)

                        try:
                            profile = Profile.objects.get(user=user_obj)
                        except Exception as e:
                            print(e)

                        messages.warning(request, 'You Need to Verify yout Email With OTP!!!')
                        send_otp(profile)
                        return redirect('profiles:otp_verification')
                else:
                    messages.info(request, 'Type correct password!!!')
                    return redirect('profiles:user_login')

        context = {
            'form': form,
        }
        return render(request, 'users_app/login.html', context)
    else:
        return redirect('posts:homepage')

@login_required
def user_logout(request):
    logout(request)
    return redirect('profiles:user_login')

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    update_avatar_form = UpdateProfileImage(request.FILES or None)
    update_cover_image = UpdateCoverImage(request.FILES or None)
    update_profile_info = UpdateProfileInfo()

    context = {
        'form_avatar': update_avatar_form,
        'cover_image_form': update_cover_image,
        'profile_info': update_profile_info,
        'profile': profile,
    }
    return render(request, 'profiles/profile.html', context)

@login_required
def get_profile(request, *args, **kwargs):
    profile = Profile.objects.get(user=kwargs.get('profile_id'))
    context = {}
    context['profile'] = profile
    return render(request, 'profiles/profile.html', context)

@login_required
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

@login_required
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

@login_required
def update_profile_info(request):
    
    data = {}
    profile = Profile.objects.get(user=request.user)

    if request.is_ajax():
        bio = request.POST.get('bio')
        # dob = request.POST.get('dob')
        profession = request.POST.get('profession')


        print('Bio: ', bio)
        print('profession: ', profession)
        profile.bio = bio
        # profile.dob_date = dob
        profile.profession = profession
        profile.save()

    data = serializers.serialize('json', [profile,])
    return JsonResponse({'data': data})