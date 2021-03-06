from django.urls import path
from .import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_view, name='profile_view'),
    path('friends/<str:profile_id>', views.get_profile, name='get_profile'),

    path('update_profile_view/', views.update_profile_image, name='update_avatar'),
]
