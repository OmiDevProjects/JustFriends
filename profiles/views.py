from django.shortcuts import render
from .models import Profile
from django.views.generic import TemplateView, View
from django.http import JsonResponse
from .forms import UpdateProfileImage

def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    update_avatar_form = UpdateProfileImage(request.FILES or None)

    context = {
        'form_avatar': update_avatar_form,
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

        if pic_id is None:
            if Post_form.is_valid():
                obj = Post_form.save(commit=False)
        else:
            obj = Post.objects.get(id=pic_id)

        obj.action = action
        obj.save()

        data = serializers.serialize('json', [obj,])
        return JsonResponse({'data': data})

    return JsonResponse()
