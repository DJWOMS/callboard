from django.urls import path

from . import views


urlpatterns = [
    path("<slug:slug>/", views.ProfileDetail.as_view(), name="profile-detail")
]