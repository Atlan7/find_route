from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


class UserResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Input your email',
            }
        )
    )


class UserConfirmPasswordResetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    new_password2 = forms.CharField(
        label='New password confirmation',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

