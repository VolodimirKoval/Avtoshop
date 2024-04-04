from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control py-4", "placeholder": "Введіть ім'я користувача"}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control py-4", "placeholder": "Введіть пароль"}
    ))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control py-4", "placeholder": "Введіть ім'я"}
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control py-4", "placeholder": "Введіть прізвище"}
    ))
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control py-4", "placeholder": "Введіть ім'я користувача"}
    ))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={"class": "form-control py-4", "placeholder": "Введіть адресу електроної пошти"}
    ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control py-4", "placeholder": "Введіть пароль"}
    ))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control py-4", "placeholder": "Підтвердіть пароль"}
    ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    # def clean_password1(self):
    #     password1 = self.cleaned_data.get("password1")
    #     if len(password1) < 8:
    #         raise ValidationError("Password must be at least 8 characters long.")
    #     if not any(char.isupper() for char in password1):
    #         raise ValidationError("Password must contain at least one uppercase letter.")
    #     return password1


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control py-4"}
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control py-4"}
    ))
    image = forms.ImageField(widget=forms.FileInput(
        attrs={"class": "custom-file-input"}
    ), required=False)
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control py-4", "readonly": True}
    ))
    email = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control py-4", "readonly": True}
    ))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')