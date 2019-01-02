from django import forms
from django.core import validators
from django.core.cache import cache
from .helpers import Helper
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password, make_password
from .models import Profile, Phone
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

    def generate_acceppted_code(self):
        accept_code = str(randint(helper.MIN_PASS_VAL, helper.MAX_PASS_VAL))

        while True:
            if cache.get(accept_code):
                accept_code = str(randint(helper.MIN_PASS_VAL, helper.MAX_PASS_VAL))
            else:
                break

        print("password::", accept_code, "phone:", self.cleaned_data.get("phone"))
        #TODO: add send in sms password on phone.
        cache.set(accept_code, self.cleaned_data.get("phone"))
        return accept_code


class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = {
            'accept_code'
        }

    phone = ""
    accept_code = forms.IntegerField(
        label='Accept Code',
        min_value=helper.MIN_PASS_VAL, max_value=helper.MAX_PASS_VAL,
        widget=forms.NumberInput()
    )

    def is_valid(self):
        super(ProfileForm, self).is_valid()

        accept_code_key = str(self.cleaned_data.get("accept_code"))
        print("accept_code:::::::::::::::::::::::::::::::::", accept_code_key)
        self.phone = cache.get(accept_code_key)
        if not self.phone:
            raise ValueError("Accept Code not allowed!")

        return True

    def get_profile_by_phone(self):
        try:
            phone = Phone.objects.filter(number=self.phone).first()
            profile = phone.profile
            if not phone:
                return None
            return profile
        except Exception as exception:
            return None

    def save(self, commit=True):
        try:
            profile = Profile()
            user = User()
            user.username = self.phone
            password = make_password(self.phone)
            user.password = password
            user.save()
            profile.user = user
            if commit:
                profile.save()
                new_phone = Phone()
                new_phone.number = self.phone
                new_phone.profile = profile
        except Exception as exception:
            return None
        return profile

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

        user = Profile(
            phone=self.phone,
            password=self.password2,
            name=self.name,
            deleted=self.deleted,
            avatar=self.avatar
        )

        if commit:
            user.save()

    class Meta:
        model = Profile
        fields = {
            'name',
            'phone',
            'email',
            'avatar',
            'deleted'
        }

