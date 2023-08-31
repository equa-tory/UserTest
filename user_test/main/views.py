from typing import Any, Dict
from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from .forms import *
from .models import *
from .utils import *

# Create your views here.



#----------------------------------------------------------------------------------------------------------------#

def index(request):
    return redirect('news')

def news(request):
    data = {
        'title': 'News',
        'menus': menus,
    }

    return render(request, 'main/news.html', context=data)

def msg(request):
    data = {
        'title': 'Messages',
        'menus': menus,
    }

    return render(request, 'main/messages.html', context=data)

def profile(request):
    data = {
        'title': 'Profile',
        'menus': menus,
    }

    return render(request, 'main/profile.html', context=data)

def settings(request):
    data = {
        'title': 'Settings',
        'menus': menus,
    }

    return render(request, 'main/settings.html', context=data)


# def reg(request):
#     data = {
#         'title': 'Registration',
#         'menus': menus,
#     }

#     return render(request, 'main/reg.html', context=data)

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/reg.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Registation")
        return dict(list(context.items()) + list(c_def.items()))
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('news')
    
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Login")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('news')
    
def  logout_user(request):
    logout(request)
    return redirect('login')

# def login(request):
#     data = {
#         'title': 'Login',
#         'menus': menus,
#     }

#     return render(request, 'main/login.html', context=data)

#----------------------------------------------------------------------------------------------------------------#


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found!</h1>')