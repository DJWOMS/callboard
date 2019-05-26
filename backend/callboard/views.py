from rest_framework import generics
from rest_framework import permissions

from .models import Advert
from .serializers import AdvertListSer, AdvertDetailSer


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
