from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView

from .forms import UserRegistrationForm
from django.conf import settings 

from django.contrib.auth import authenticate, login


class SignupView(FormView):
	form_class = UserRegistrationForm
	success_url = '/'
	template_name = 'MainApp/mainpage.html'

	def form_valid(self, form):
		user = form.save(commit=False)
		user.set_password(form.cleaned_data['password1'])
		user.save()
		return super().form_valid(form)


class LoginView(FormView):
	form = UserRegistrationForm
	success_url = '/'
	template_name = 'MainApp/mainpage.html'

	def is_valid(self, form):
		cd = form.cleaned_data
		user = authenticate(email=cd['email'], password=cd['password1'])
		if user.is_active():
			login(self.request, user)
			return super().is_valid(form)
		else:
			return HttpResponse('Disable account')


class LogoutView(FormView):
	success_url = '/'
	