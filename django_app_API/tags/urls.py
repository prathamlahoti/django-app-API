from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import TagsList


router = routers.DefaultRouter()
router.register('tags', TagsList)

urlpatterns = [
    path('', include(router.urls)),
]
