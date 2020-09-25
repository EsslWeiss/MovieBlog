from django.urls import path
from MainApp.views import MainView


urlpatterns = [
	path('', MainView.as_view(), name='MainPageView'),

]
