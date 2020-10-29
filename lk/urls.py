from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>', views.profile, name='profile_detail'),
    path('account/', views.account, name='account'),
    path('account/update/', views.update_params, name='api_update_params'),
    path('diary/posts/', views.get_diary_list, name='api_diary'),
    path('accounts/login/', views.main_redirect_view, name='main_redirect'),
]