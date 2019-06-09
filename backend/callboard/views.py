from rest_framework import generics
from rest_framework import permissions

from .models import Advert
from .serializers import AdvertListSer, AdvertDetailSer, AdvertCreateSer


class AdvertList(generics.ListAPIView):
    """Все объявления"""
    permission_classes = [permissions.AllowAny]
    queryset = Advert.objects.all()
    serializer_class = AdvertListSer


class AdvertDetail(generics.RetrieveAPIView):
    """Подробно об объявлении"""
    permission_classes = [permissions.AllowAny]
    queryset = Advert.objects.all()
    lookup_field = 'slug'
    serializer_class = AdvertDetailSer


class AdvertCreate(generics.CreateAPIView):
    """Добавление объявления"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Advert.objects.all()
    serializer_class = AdvertCreateSer


class UserAdvertList(generics.ListAPIView):
    """Все объявления пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdvertListSer

    def get_queryset(self):
        return Advert.objects.filter(user=self.request.user)


class UserAdvertUpdate(generics.UpdateAPIView):
    """Редактирование объявления пользователя"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdvertCreateSer

    def get_queryset(self):
        return Advert.objects.filter(user=self.request.user)


class UserAdvertDelete(generics.DestroyAPIView):
    """Удаление объявления пользователя"""
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Advert.objects.filter(id=self.kwargs.get("pk"), user=self.request.user)
