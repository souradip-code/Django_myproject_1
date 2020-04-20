from django.shortcuts import render
from basic_app import models

# from django.forms import ValidationError
from .forms import RegisterForm
from django.contrib.auth.models import User
# from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def user_login(request):
    return render(request,'basic_app/login.html')


def user_register(request):

    template = 'basic_app/register.html'

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['fullname']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['pwd1'] != form.cleaned_data['pwd2']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['fullname'],
                    form.cleaned_data['email'],
                    form.cleaned_data['pwd1']
                )
                user.contact_pref = form.cleaned_data['contact_pref']
                user.contact_suff = form.cleaned_data['contact_suff']
                user.job = form.cleaned_data['job']
                user.save()
                return render(request, 'basic_app/index.html')   

        return render(request, template,{'form': form})
    else:
        form = RegisterForm()

    return render(request,template,{'form': form})