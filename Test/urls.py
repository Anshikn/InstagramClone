from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('test', views.TestView)


urlpatterns = router.urls

# urlpatterns = [
#   path('',views.TestView.as_view()),
# ]