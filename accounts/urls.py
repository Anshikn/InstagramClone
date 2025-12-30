from django.urls import path
from .views import RegisterView, ProfileDetailView, FollowToggleView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("profile/<str:user__username>/", ProfileDetailView.as_view()),
    path("follow/<str:username>/", FollowToggleView.as_view()),
]
