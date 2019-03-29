from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import CategoriesList

router = routers.DefaultRouter()
router.register('categories', CategoriesList)

urlpatterns = [
    path('', include(router.urls)),
]