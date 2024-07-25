from django.db import models

#choices
COURSE_CHOICES = ( 
    ("BCA - Bachelor Of Computer Application", "BCA - Bachelor Of Computer Application"), 
    ("MCA - Master Of Computer Application", "MCA - Master Of Computer Application"), 
) 

SEMESTER_CHOICES = ( 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"), 
    ("6", "6"), 
    ("7", "7"), 
    ("8", "8"), 
) 

club_choices = (
    ("Technical", "Technical club"),
    ("Sports", "Sports club"),
    ("Cultural", "Cultural club"),
    ("Eco", "Eco club"),
)



# Create your models here.
class members(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    enrollment_number = models.BigIntegerField(blank=False, null=False, unique=True)
    email = models.CharField(max_length=256,blank=False, null=False, unique=True)
    course = models.CharField(max_length = 256, choices=COURSE_CHOICES)
    semester = models.CharField(max_length=256,blank=False, choices=SEMESTER_CHOICES)
    club = models.CharField(max_length=256, choices=club_choices)

    def __str__(self):
        return f"{self.name} from {self.club}"