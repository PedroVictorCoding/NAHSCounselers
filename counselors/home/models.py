from django.db import models

class Updates(models.Model):
    PAGE_TO_DISPLAY = (
        ("1", "Graduation Coach & Credit Recovery"),
        ("2", "Scholarships and Financial Aid"),
        ("3", "Summer School & Virtual School"),
        ("4", "Seniors"),
        ("5", "SAT/ACT & Test Prep Opportunities"),
        ("6", "New Enrollment"),
        ("7", "Dual Enrollment"),
        ("8", "Raising 9th Graders"),
    )
    page_to_display     = models.CharField(max_length=50, choices=PAGE_TO_DISPLAY)
    title               = models.CharField(max_length=100)
    content             = models.TextField(max_length=5000)
    image               = models.ImageField()
    external_url        = models.CharField(max_length=100, blank=True)
    counselor_name      = models.CharField(max_length=50)
    data_published   = models.DateTimeField(auto_now=True)

"""
Django Model:
Page: senior or enrollment...
Title:
Content: | linebreak
Image: (not required)

Url: (not required)
Counselor name:
Data of publishment:
(Fill data in /admin/) 

"""

