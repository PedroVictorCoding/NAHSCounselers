from django.contrib import admin
from django.urls import path, include
from home.views import home, graduation_coach

urlpatterns = [
    path('', home, name='homepage'),

    path('graduation-coach', graduation_coach, name="graduation_coach")
]
