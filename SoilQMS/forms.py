from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


# Sign In Form
class SignInForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'id': 'signin_username'})
    )
    password = forms.CharField(widget=forms.PasswordInput)


# Registration Form
class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'password1', 'password2')
