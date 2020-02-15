from django.contrib import admin
from django.urls import path, include
from forms.views import new_recommendation, StudentRecommendationView

urlpatterns = [
    path('recommendation', new_recommendation, name="new_recommendation"),
    path('recommendation/student', StudentRecommendationView.as_view(), name="student_recommendation"),
    #path('recommendation/parent', parent_recommendation, name="parent_recommendation"),
]
