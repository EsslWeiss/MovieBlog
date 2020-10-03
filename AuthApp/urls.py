from django.urls import path
from .views import SignupView


app_name = 'AppAuth'
urlpatterns = [ 
	path('sign-up/', SignupView.as_view(), name='SignupView'),
]