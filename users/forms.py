from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from django.core import validators
from .models import User

class RegisterForm(UserCreationForm):
    phone_regex = validators.RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                            message="Phone number must be entered in the format: '+70000000000'. Up to 15 digits allowed.")
    phone = forms.CharField(label='Phone', validators=[phone_regex], max_length=17, blank=True)

    class Meta:
        model = User
        fields = {
            'phone'
        }

    def save(self, commit=True):
        user = User(phone=self.phone, password=self.password2)

        if commit:
            user.save()

class UserParametersForm(UserChangeForm):
    names_regex = validators.RegexValidator(regex=r'^[-a-zA-Z0-9_]+$',
                                            message="Hier must be entered symbols: -_, a-z, A-Z, 0-9.")

    email_valid = validators.EmailValidator(message="Email not valid symbols.")

    phone_regex = validators.RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                            message="Phone number must be entered in the format: '+70000000000'. Up to 15 digits allowed.")

    phone = forms.CharField(label='Phone', validators=[phone_regex], max_length=17, blank=True)

    name = forms.CharField(label='Name', max_length=17, blank=True)

    email = forms.EmailField(label='Email', max_length=90, blank=True, validators=[email_valid])

    avatar = forms.ImageField(allow_empty_file=True, label="Avatar")

    deleted = forms.BooleanField(label="Delete User")


    def save(self, commit=True):

        user = User(
            phone=self.phone,
            password=self.password2,
            name=self.name,
            deleted=self.deleted
        )

        if commit:
            user.save()

    class Meta:
        model = User
        fields = {
            'name',
            'phone',
            'email',
            'avatar',
            'delete'
        }