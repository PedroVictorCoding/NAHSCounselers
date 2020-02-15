from django import forms
from .models import StudentRecommendation

class StudentRecommendationForm(forms.ModelForm):
    student_first_name  = forms.CharField(max_length=30, required=True)
    student_last_name   = forms.CharField(max_length=30, required=True)
    student_email       = forms.EmailField(required=True)
    student_cellphone   = forms.CharField(max_length=15, required=False)
    COUNSELORS_OPTIONS = (
        ("1", "Ms. Marino"),
        ("2", "Mr. Robinson"),
    )
    counselor_name      = forms.RadioSelect(choices=COUNSELORS_OPTIONS)
    college_deadline    = forms.CharField(max_length=50, required=True)
    college_name        = forms.CharField(max_length=100, required=False)
    DELIVERY_OPTIONS     = (
        ("GEORGIA_UNIVERSITY", "Georgia College/ University"),
        ("COMMONAPP", "Common App"),
        ("ONLINE_PORTAL", "Online Portal"),
        ("PAPER", "Paper/ Hard Copy"),
    )
    delivery_option     = forms.RadioSelect(choices=DELIVERY_OPTIONS)

    class Meta:
        model = StudentRecommendation
        fields = (
            'student_first_name',
            'student_last_name',
            'student_email',
            'student_cellphone',
            'counselor_name',
            'college_deadline',
            'college_name',
            'delivery_option',

        )