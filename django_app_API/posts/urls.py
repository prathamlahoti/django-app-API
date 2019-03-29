from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import PostsList


router = routers.DefaultRouter()
router.register('posts', PostsList)

urlpatterns = [
    path('', include(router.urls)),
]
