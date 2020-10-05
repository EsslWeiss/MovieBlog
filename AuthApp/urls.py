from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
	UserSignupView, UserLoginView, UserLogoutView, UserPasswordChangeView
)
from django.contrib.auth import views as auth_views 


app_name = 'AppAuth'
urlpatterns = [ 
	path('sign-up/', UserSignupView.as_view(), name='UserSignupView'),
	path('log-in/', UserLoginView.as_view(), name='UserLoginView'), 
	path('log-out/', UserLogoutView.as_view(), name='UserLogoutView'),
	
	paht('password-change/done/', 
		auth_views.PasswordChangeDoneView.as_view(), 
		name='password_change_done'),

	path('password-change/', auth_views.PasswordChangeView.as_view(), 
		name='password_change'),
	
	path('password-reset/done/', auth_views.PasswordResetCompleteView.as_view(),
		name='password_reset_complete'),

	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
		name='password_reset'),

	path('password-reset/', auth_views.PasswordResetView.as_view(), 
		name='')
]