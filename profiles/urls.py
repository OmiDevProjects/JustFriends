from django.urls import path
from .import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_view, name='profile_view'),
    path('friends/<str:profile_id>', views.get_profile, name='get_profile'),

    path('update_profile_view/', views.update_profile_image, name='update_avatar'),
    path('update_coverImage/', views.update_cover_image, name='update_coverImage'),

    # User Authentication
    path('register/', views.user_register_form, name='user_register'),
    path('login/', views.user_login_form, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
