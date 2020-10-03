from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django.conf import settings 


class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('email', )


class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = ('email', )


class UserRegistrationForm(forms.ModelForm):
	password1 = forms.CharField(label='password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='password repeat', widget=forms.PasswordInput)

	def clean_password2(self):
		cleaned = self.cleaned_data
		if cleaned['password1'] != cleaned['password2']: 
			raise forms.ValidationError('passwords dont match.')
		return cleaned['password2']

	class Meta:
		model = CustomUser
		fields = ('email', 'password1', 'password2')

