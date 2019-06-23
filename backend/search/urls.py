from django.urls import path

from .views import *


urlpatterns = [
    path("", SearchAdvert.as_view())
]