from django.shortcuts import render
from .models import Profile
from django.views.generic import TemplateView, View
from django.http import JsonResponse

def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    context = {}
    context['profile'] = profile
    return render(request, 'profiles/profile.html', context)

def get_profile(request, *args, **kwargs):
    profile = Profile.objects.get(user=kwargs.get('profile_id'))
    context = {}
    context['profile'] = profile
    return render(request, 'profiles/profile.html', context)

class MyProfileView(TemplateView):
    template_name = 'profiles/my_profile.html'

class MyProfileData(View):
    def get(self, *args, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        qs = profile.proposals_for_following()

        profiles_to_follow_list = []
        for user in qs:
            p = Profile.objects.get(user__username=user.username)
            profile_item = {
                'id': p.id,
                'user': p.user.username,
                'avatar': p.avatar.url,
            }
            profiles_to_follow_list.append(profile_item)

        return JsonResponse({'data': profiles_to_follow_list})