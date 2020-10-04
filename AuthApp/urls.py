from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
	UserSignupView, UserLoginView, UserLogoutView, 
)


app_name = 'AppAuth'
urlpatterns = [ 
	path('sign-up/', UserSignupView.as_view(), name='UserSignupView'),
	path('log-in/', UserLoginView.as_view(), name='UserLoginView'), 
	path('log-out/', UserLogoutView.as_view(), name='UserLogoutView'),
]