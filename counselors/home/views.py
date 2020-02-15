from django.shortcuts import render
from home.models import Updates

def home(request):
    return render(request, 'home/home.html')

def graduation_coach(request):
    graduation_updates = Updates.objects.filter(page_to_display="1")
    args = {'graduation_updates': graduation_updates}
    return render(request, 'home/graduation-coach.html', args)
