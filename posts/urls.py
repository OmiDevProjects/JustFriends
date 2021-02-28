from django.urls import path
from .import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='homepage'),

    #EndPoints
    path('json-posts/', views.post_json_response, name='posts-view-json'),
]