from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.utils.http import is_safe_url

from .forms import LoginForm, RegisterForm, RegisterstaffForm

# Create your views here. 

User = get_user_model()

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    next_=request.GET.get('next')
    next_post =request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        else:
            request.session['invalid_user'] = 1
    return render(request, 'accounts/login.html', context)

def register_page(request):
     form = RegisterForm(request.POST or None)
     context = {
         "form": form
     }
     if form.is_valid():
         form.save()
         return redirect("/")
     return render(request, 'accounts/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/login')

def registerstaff_view(request):
    form = RegisterstaffForm(request.POST or None)
    context = {
         "form": form
     }
    if form.is_valid():
         form.save()
         return redirect("/")
    return render(request, 'accounts/registerseller.html', context)
                