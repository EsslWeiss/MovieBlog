from django.template.loader import get_template
from django import template
from AuthApp.forms import SigninForm, LoginForm

register = template.Library()

@register.inclusion_tag('AuthApp/tags/authenticate_bar_template.html')
def authentication_bar():
	context = {'login_form': LoginForm, 'signup_form': SigninForm}
	return context
