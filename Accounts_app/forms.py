from django import forms
from django.contrib.auth.forms import UserCreationForm
from Accounts_app.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label='password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )
    first_name = forms.CharField(label='Forename')
    last_name = forms.CharField(label='Surname')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        exclude = {'username'}

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)

        instance.username = instance.email

        if commit:
            instance.save()

        return instance


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class PersonalDetailsForm(forms.Form):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Forename')
    last_name = forms.CharField(label='Surname')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        exclude = {'username'}

    def save(self, commit=True):
        instance = super(PersonalDetailsForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance