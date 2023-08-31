from django.urls import path, re_path
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', index, name='redir'),
    path('news/', news, name='news'),
    path('msg/', msg, name='msg'),
    path('profile/', profile, name='profile'),
    path('settings/', settings, name='settings'),
    path('reg/', RegisterUser.as_view(), name='reg'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
