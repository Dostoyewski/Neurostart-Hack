from django.urls import path

from . import views

urlpatterns = [
    path('', views.competitions_list, name='competition_list'),
    path('<slug:slug>', views.video_recording, name='video_rec'),
]