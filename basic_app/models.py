from django.db import models
from django.contrib.auth.models import User

# Create your models here.

JOB_CHOICES = (
    (1, "Designer"),
    (2, "Manager"),
    (3, "Accounting")
)
CONTACT_CHOICES = (
    (1, "+91"),
    (2, "+92"),
    (3, "+93"),
)

class UserInfoModel(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    fullname = models.CharField(max_length=264,unique=True)
    email = models.EmailField(max_length=255)
    contact_pref = models.IntegerField(choices=CONTACT_CHOICES, default=1)
    contact_suff =models.IntegerField()
    job= models.IntegerField(choices=JOB_CHOICES, default=1)
    pwd1 = models.CharField(max_length=20)
    pwd2 = models.CharField(max_length=20)

    def __str__(self):
        return user.fullname
