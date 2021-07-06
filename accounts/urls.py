from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *
from .forms import *


urlpatterns = [
    path('registration/', UserRegistration.as_view(), name='registration'),
    path('login/', UserAuthentication.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='accounts/reset_password.html',
        email_template_name='accounts/password_reset_email.html',
        form_class=UserResetPasswordForm,
        success_url=reverse_lazy('accounts:password_reset_done')),
        name='reset_passoword'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        form_class=UserConfirmPasswordResetForm,
        success_url=reverse_lazy('accounts:password_reset_complete')),
        name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'),
]
