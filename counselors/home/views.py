from django.shortcuts import render
from home.models import Updates

def home(request):
    return render(request, 'home/home.html')

def graduation_coach(request):
    graduation_updates = Updates.objects.filter(page_to_display="1")
    args = {'graduation_updates': graduation_updates}
    return render(request, 'home/graduation-coach.html', args)

def scholarships_and_financial_aid(request):
    scholarships_updates = Updates.objects.filter(page_to_display="2")
    args = {'scholarships_updates': scholarships_updates}
    return render(request, 'home/scholarships_and_financial_aid.html', args)

def summer_school_and_virtual_school(request):
    summer_updates = Updates.objects.filter(page_to_display="3")
    args = {'summer_updates': summer_updates}
    return render(request, 'home/summer.html', args)

def seniors(request):
    seniors_updates = Updates.objects.filter(page_to_display="4")
    args = {'seniors_updates': seniors_updates}
    return render(request, 'home/seniors.html', args)

def sat_act(request):
    sat_act_updates = Updates.objects.filter(page_to_display="5")
    args = {'sat_act_updates': sat_act_updates}
    return render(request, 'home/sat_act.html', args)

def new_enrollment(request):
    new_enrollment_updates = Updates.objects.filter(page_to_display="6")
    args = {'new_enrollment_updates': new_enrollment_updates}
    return render(request, 'home/new_enrollment.html', args)

def dual_enrollment(request):
    dual_enrollment_updates = Updates.objects.filter(page_to_display="7")
    args = {'dual_enrollment_updates': dual_enrollment_updates}
    return render(request, 'home/dual_enrollment.html', args)

def nineth_graders(request):
    nineth_graders_updates = Updates.objects.filter(page_to_display="8")
    args = {'nineth_graders_updates': nineth_graders_updates}
    return render(request, 'home/nineth_graders.html', args)