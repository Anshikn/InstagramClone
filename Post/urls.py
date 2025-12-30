from django.urls import path
from .views import (
    PostCreateView,
    FeedView,
    LikeToggleView,
    CommentCreateView,
)

urlpatterns = [
    path("create/", PostCreateView.as_view()),
    path("feed/", FeedView.as_view()),
    path("<int:post_id>/like/", LikeToggleView.as_view()),
    path("<int:post_id>/comment/", CommentCreateView.as_view()),
]
