from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from django.views.generic.edit import FormView

from django.contrib.auth.views import (
	LoginView, LogoutView
) 

from django.contrib.auth.forms import UserChangeForm, PasswordResetForm
from django.contrib.auth.views import PasswordChangeView
from .forms import SigninForm, LoginForm

from django.contrib.auth import authenticate, login, logout
from django.conf import settings


class UserSignupView(FormView):
	form_class = SigninForm
	success_url = '/'
	template_name = 'MainApp/mainpage.html'
	auth_backend = 'AuthApp.backends.EmailOnlyBackend'

	def form_valid(self, form):
		user = form.save(commit=False)
		user.save()
		login(self.request, user, backend=self.auth_backend)
		return HttpResponseRedirect(self.success_url)


class UserLoginView(LoginView):
	template_name='MainApp/mainpage.html'
	success_url = reverse_lazy('MainApp:MainPageView')
	form_class = LoginForm
	auth_backend = 'AuthApp.backends.EmailOnlyBackend'

	def get_success_url(self):
		return self.success_url or self.request.path

	def form_valid(self, form):
		cd = form.cleaned_data
		user = authenticate(request=self.request, 
			email=cd['username'], 
			password=cd['password'])
		if user.is_active:
			login(self.request, user, backend=self.auth_backend)
		return HttpResponseRedirect(self.get_success_url())


class UserLogoutView(LogoutView):

	def get_next_page(self):
		if self.next_page is not None:
			next_page = reverse_lazy(self.next_page)
		elif settings.LOGOUT_REDIRECT_URL:
			next_page = settings.LOGOUT_REDIRECT_URL
		else:
			next_page = self.request.path
		return next_page

	def dispatch(self, request, *args, **kwargs):
		if not request.user:
			return HttpResponse('User not found! check your middleware.')
		logout(request)
		next_page = self.get_next_page()
		if next_page:
			return HttpResponseRedirect(next_page)
		return super().dispatch(request, *args, **kwargs)


class UserPasswordChangeView(PasswordChangeView):
	template_name='MainApp/mainpage.html'
	success_url = reverse_lazy('MainApp:MainPageView')
	form_class = UserChangeForm

	def form_valid(self, form):
		pass