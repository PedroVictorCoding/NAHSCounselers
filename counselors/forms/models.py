from django.db import models

class StudentRecommendation(models.Model):
    #User Inputed data
    student_first_name  = models.CharField(max_length=50)
    student_last_name   = models.CharField(max_length=50)
    student_email       = models.EmailField(max_length=254)
    student_cellphone   = models.CharField(max_length=20)
    COUNSELORS_OPTIONS  = (
        ("1", "Ms. Marino"),
        ("2", "Mr. Robinson"),
    )
    counselor_name      = models.CharField(max_length=50, choices=COUNSELORS_OPTIONS)
    college_deadline    = models.CharField(max_length=50)
    college_name        = models.CharField(max_length=100)
    DELIVERY_OPTIONS     = (
        ("GEORGIAUNIVERSITY", "Georgia College/ University"),
        ("COMMONAPP", "Common App"),
        ("ONLINEPORTAL", "Online Portal"),
        ("PAPER", "Paper/ Hard Copy"),
    )
    delivery_option     = models.CharField(max_length=50, choices=DELIVERY_OPTIONS)

    #Not Inputed by User data
    date_request        = models.DateTimeField(auto_now_add=True)



