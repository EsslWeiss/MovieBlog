from django import forms
from django.contrib.auth.forms import (
	UserCreationForm, UserChangeForm, PasswordResetForm
)

from .models import CustomUser
from django.conf import settings 
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('email', )


class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = ('email', )


class SigninForm(forms.ModelForm):
	password1 = forms.CharField(label='password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='password repeat', widget=forms.PasswordInput)

	def clean_password2(self):
		cleaned = self.cleaned_data
		if cleaned['password1'] != cleaned['password2']: 
			raise forms.ValidationError('passwords dont match.')
		return cleaned['password2']

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

	class Meta:
		model = CustomUser
		fields = ('email', 'password1', 'password2')


class LoginForm(AuthenticationForm):

	class Meta:
		model = CustomUser
		fields = ('email', 'password')

