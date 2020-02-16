from django.contrib import admin
from django.urls import path, include
from home.views import home, graduation_coach
from home.views import scholarships_and_financial_aid
from home.views import summer_school_and_virtual_school
from home.views import seniors, sat_act, new_enrollment, dual_enrollment
from home.views import nineth_graders

urlpatterns = [
    path('', home, name='homepage'),

    path('graduation-coach', graduation_coach, name="graduation_coach"),
    path('scholarships-and-financial-aid', scholarships_and_financial_aid, name="scholarships-and-financial-aid"),
    path('summer-school-and-virtual-school', summer_school_and_virtual_school, name="summer-school-and-virtual-school"),
    path('seniors', seniors, name="seniors"),
    path('sat-act', sat_act, name="sat_act"),
    path('new-enrollment', new_enrollment, name="new_enrollment"),
    path('dual-enrollment', dual_enrollment, name="dual_enrollment"),
    path('nineth-graders', nineth_graders, name="nineth_graders"),
]
