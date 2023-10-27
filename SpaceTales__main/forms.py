from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models


class UserForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "phone",
        )

    email = forms.EmailField(
        max_length=250,
        required=True,
        help_text="Enter a valid email address, for example: 2nEoJ@example.com",
        label="Email",
    )

    phone = forms.CharField(
        max_length=15,
        required=False,
        help_text="Phone number must contain only 11 digits in format _(___)___-__-__",
        label="Phone",
    )
