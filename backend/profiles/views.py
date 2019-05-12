from django.shortcuts import render
from django.views.generic import DetailView

from .models import Profile


class ProfileDetail(DetailView):
    """Профиль пользователя"""
    model = Profile
    context_object_name = "profile"
    template_name = "profiles/user-detail.html"
