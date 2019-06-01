from django.urls import path

from . import views


urlpatterns = [
    path("<int:pk>/", views.ProfileDetail.as_view()),
    path("update/<int:pk>/", views.ProfileUpdateView.as_view()),
]