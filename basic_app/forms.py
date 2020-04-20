
from django import forms
from basic_app.models import UserInfoModel
from django.contrib.auth.models import User

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

class RegisterForm(forms.ModelForm):

    fullname = forms.CharField(max_length=264,widget=forms.TextInput(attrs={'class':'form-control'}))

    email = forms.EmailField(max_length=255,widget=forms.EmailInput(attrs={'class':'form-control'}))

    contact_pref = forms.ChoiceField(choices=CONTACT_CHOICES,widget=forms.Select(attrs={'class':'custom-select'}))

    contact_suff =forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    job= forms.ChoiceField(choices=JOB_CHOICES,widget=forms.Select(attrs={'class':'custom-select'}))

    pwd1 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control'}))

    pwd2 = forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = UserInfoModel
        # fields = "__all__"
        exclude =("user",)