from django.contrib import admin
from forms.models import StudentRecommendation
from home.models import Updates

admin.site.site_header  = "Counselor's Page"
admin.site.site_title   = "Counselor's Page"
admin.site.index_title  = "Counselor's Data"

class StudentRecommendationAdmin():
       list_display = ('first_name', 'last_name')
       list_filter = ('date')


admin.site.register(StudentRecommendation, StudentRecommendationAdmin)
admin.site.register(Updates)
admin.site.unregister(Groups)
