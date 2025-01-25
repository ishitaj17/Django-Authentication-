# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

class CustomPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    success_url = '/password_reset/done/'  # Redirect after successful email submission


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use the custom form
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = CustomUserCreationForm()  # Instantiate an empty form for GET requests
    return render(request, 'users/signup.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = '/reset/done/'  # Redirect after password change

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'
    


def custom_logout(request):
    if request.method == 'POST':  # Handle POST requests to log the user out
        logout(request)  # Logs the user out
        return redirect('login')  # Redirect to login page after logout
    # Optionally, allow GET requests for logout, but ideally POST should be used for logout
    elif request.method == 'GET':
        logout(request)
        return redirect('login')  # Redirect to login page after logout
    else:
        return HttpResponseForbidden("Forbidden")  # Handle unsupported request methods


