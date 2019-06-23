from django.db.models import Q
from rest_framework import generics, permissions

from backend.callboard.models import Advert
from backend.callboard.serializers import AdvertListSer


class SearchAdvert(generics.ListAPIView):
    """Все объявления"""
    permission_classes = [permissions.AllowAny]
    serializer_class = AdvertListSer

    def get_queryset(self):
        search = self.request.GET.get("search")
        filters = []
        a = Q()
        try:
            a |= Q(price=float(search))
        except ValueError:
            pass
        a |= Q(subject__icontains=search)
        a |= Q(category__name__icontains=search)
        a |= Q(filters__name__icontains=search)
        a |= Q(user__profile__email_two=search)
        a |= Q(user__profile__phone=search)
        a |= Q(user__profile__first_name=search)
        a |= Q(user__profile__last_name=search)
        filters.append(a)
        return Advert.objects.filter(*filters)
