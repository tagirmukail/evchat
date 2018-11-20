from django import forms
from django.core import validators
from django.core.cache import cache
from .helpers import Helper
from .models import UserProfile
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
        password = str(randint(helper.MIN_PASS_VAL, helper.MAX_PASS_VAL))

        while True:
            if cache.get(password):
                password = str(randint(helper.MIN_PASS_VAL, helper.MAX_PASS_VAL))
            else:
                break

        print("password::", password, "phone:", self.cleaned_data.get("phone"))

        cache.set(password, self.cleaned_data.get("phone"))
        return password

class RegisterForm(forms.Form):
    class Meta:
        model = UserProfile
        fields = {
            'password'
        }

    password = forms.IntegerField(label='Password', min_value=helper.MIN_PASS_VAL, max_value=helper.MAX_PASS_VAL)

    def save(self, commit=True):
        pass_key = str(self.cleaned_data.get("password"))
        phone = cache.get(pass_key)
        if not phone:
            return None

        user = UserProfile(phone=phone)

        if commit:
            user.save()
        return user

class UserParametersForm(forms.Form):
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

        user = UserProfile(
            phone=self.phone,
            password=self.password2,
            name=self.name,
            deleted=self.deleted,
            avatar=self.avatar
        )

        if commit:
            user.save()

    class Meta:
        model = UserProfile
        fields = {
            'name',
            'phone',
            'email',
            'avatar',
            'deleted'
        }

