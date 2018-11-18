from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django import forms
from django.core import validators
from django.core.cache import cache
from .helpers import Helper
from .models import User
from random import randint

helper = Helper()

class SendForm(forms.Form):
    class Meta:
        fields = {
            'phone'
        }

    phone_regex = validators.RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                            message="Phone number must be entered in the format: '+70000000000'. Up to 15 digits allowed.")
    phone = forms.CharField(label='Phone', validators=[phone_regex], max_length=17)

    def generate_acceppted_pass(self):
        password = randint(100001, 999998)

        while True:
            if cache.get(password):
                password = randint(100001, 999998)
            else:
                break

        print("password::", password, "phone:", self.cleaned_data.get("phone"))

        cache.set(password, self.cleaned_data.get("phone"), 30)
        return password

class RegisterForm(forms.Form):
    class Meta:
        model = User
        fields = {
            'password'
        }

    password = forms.IntegerField(label='Password', min_value=100001, max_value=999998)

    def save(self, commit=True):
        phone = cache.get(self.cleaned_data.get("password"))
        if not phone:
            return None

        user = User(phone=phone)

        if commit:
            user.save()
        return user

class UserParametersForm(UserChangeForm):
    names_regex = validators.RegexValidator(regex=r'^[-a-zA-Z0-9_]+$',
                                            message="Hier must be entered symbols: -_, a-z, A-Z, 0-9.")

    email_valid = validators.EmailValidator(message="Email not valid symbols.")

    phone_regex = validators.RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                            message="Phone number must be entered in the format: '+70000000000'. Up to 15 digits allowed.")

    phone = forms.CharField(label='Phone', validators=[phone_regex], max_length=17)

    name = forms.CharField(label='Name', max_length=17)

    email = forms.EmailField(label='Email', max_length=90, validators=[email_valid])

    avatar = forms.ImageField(allow_empty_file=True, label="Avatar")

    deleted = forms.BooleanField(label="Delete User")


    def save(self, commit=True):

        user = User(
            phone=self.phone,
            password=self.password2,
            name=self.name,
            deleted=self.deleted,
            avatar=self.avatar
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
            'deleted'
        }

