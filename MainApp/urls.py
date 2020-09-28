from django.urls import path
from MainApp.views import (MainPageView, MovieView, SearchManager,
	PersonView, MovieFilterView)


urlpatterns = [
	path('', MainPageView.as_view(), name='MainPageView'),
	path('movie-catalog/', MovieView.as_view(), name='MovieView'),
	path('person-catalog/', PersonView.as_view(), name='PersonView'),

	path('filter/', MovieFilterView.as_view(), name='MovieFilterView'),
	path('search/', SearchManager.as_view(), name='SearchManager'),
]
