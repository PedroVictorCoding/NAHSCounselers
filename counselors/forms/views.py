from django.shortcuts import render, HttpResponseRedirect
import json
from django.views.generic import TemplateView

from .models import StudentRecommendation
from .forms import StudentRecommendationForm

def new_recommendation(request):
    return render(request, 'forms/new_recommendation.html')

def student_recommendation(request):

    return render(request, 'forms/student_recommendation.html')

class StudentRecommendationView(TemplateView):
    template_name = 'forms/student_recommendation.html'

    def get(self, request):
        form        = StudentRecommendationForm()
        args            = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = StudentRecommendationForm(request.POST)
        if form.is_valid():
            student_first_name  = form.cleaned_data['student_first_name']
            student_last_name   = form.cleaned_data['student_last_name']
            student_email       = form.cleaned_data['student_email']
            student_cellphone   = form.cleaned_data['student_cellphone']
            counselor_name      = form.cleaned_data['counselor_name']
            college_deadline    = form.cleaned_data['college_deadline']
            college_name        = form.cleaned_data['college_name']
            delivery_option     = form.cleaned_data['delivery_option']
            form.save()
            form        = StudentRecommendationForm()
            return HttpResponseRedirect('/')
        args        = {'form': form}
        return render(request, self.template_name, args)





def parent_recommendation(request):
    return render(request, 'forms/parent_recommendation.html')