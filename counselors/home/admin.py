from django.contrib import admin
from forms.models import StudentRecommendation
from home.models import Updates

admin.site.site_header  = "Counselor's Page"
admin.site.site_title   = "Counselor's Page"
admin.site.index_title  = "Counselor's Data"


admin.site.register(StudentRecommendation)
admin.site.register(Updates)
