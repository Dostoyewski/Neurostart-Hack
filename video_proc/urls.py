from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('', views.competitions_list, name='competition_list'),
    path('<slug:slug>', views.video_recording, name='video_rec'),
    # path('account/', views.account, name='account'),
    # path('account/update/', views.update_params, name='api_update_params'),
    # path('diary/posts/', views.get_diary_list, name='api_diary'),
    # path('accounts/login/', views.main_redirect_view, name='main_redirect'),
    # path('news/', views.news_list, name='news_list'),
]