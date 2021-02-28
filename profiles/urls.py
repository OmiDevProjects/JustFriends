from django.urls import path
from .import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_view, name='profile_view'),
    path('friends/<str:profile_id>', views.get_profile, name='get_profile'),

    path('my_profile/', views.MyProfileView.as_view(), name='my-profile-view'),
    path('my_profile_json/', views.MyProfileData.as_view(), name='my-profile-data'),
]
