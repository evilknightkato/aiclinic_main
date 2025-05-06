from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import CustomUser

def home(request):
    return render(request, 'clients/home.html')

def about(request):
    return render(request, 'clients/about.html')

@login_required
def client_page(request):
    return render(request, 'clients/client_page.html')

@login_required
def staff_page(request):
    if not request.user.is_staff_member:
        return redirect('client_page')
    users = CustomUser.objects.filter(is_staff_member=False)
    return render(request, 'clients/staff_page.html', {'users': users})

class CustomLoginView(LoginView):
    template_name = 'clients/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'clients/logged_out.html'

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile_redirect')
    else:
        form = RegisterForm()
    return render(request, 'clients/register.html', {'form': form})

@login_required
def profile_redirect(request):
    if request.user.is_staff_member:
        return redirect('staff_page')
    return redirect('client_page')