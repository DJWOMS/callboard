from rest_framework import generics
from rest_framework import permissions

from .models import Profile
from .serializers import ProfileSer, ProfileUpdateSer, AvatarUpdateSer


class ProfileDetail(generics.RetrieveAPIView):
    """Профиль пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSer


class ProfileUpdateView(generics.UpdateAPIView):
    """Редактирование профилья пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSer


class AvatarProfileUpdateView(generics.UpdateAPIView):
    """Редактирование аватара профилья пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = AvatarUpdateSer


