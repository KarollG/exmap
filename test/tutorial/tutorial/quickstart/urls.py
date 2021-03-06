from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import urls
from tutorial.quickstart.viewsets import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]