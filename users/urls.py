from django.urls import path
from .views import (
    CustomLoginView,
    signup,
    dashboard,
    profile,
    change_password,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
)
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views

# urlpatterns = [
#     # Authentication URLs
#     path('login/', CustomLoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('signup/', signup, name='signup'),

#     # Dashboard and Profile
#     path('dashboard/', dashboard, name='dashboard'),
#     path('profile/', profile, name='profile'),
#     path('change_password/', change_password, name='change_password'),

#     # Password Reset URLs
#     path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
#     path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]

urlpatterns = [
    path('', CustomLoginView.as_view(), name='home'),  # Redirect root URL to login
    path('login/', CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('logout/', views.custom_logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('change_password/', change_password, name='change_password'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
