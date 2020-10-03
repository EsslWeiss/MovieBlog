from django.urls import path
from MainApp.views import (MainPageView, MovieView, SearchManager,
	PersonView, MovieFilterView, ProducerDetailView, ActorDetailView, 
	MovieDetailView)


app_name = 'MainApp'
urlpatterns = [
	path('', MainPageView.as_view(), name='MainPageView'),
	path('movie-catalog/', MovieView.as_view(), name='MovieView'),
	path('<slug:slug>/', MovieDetailView.as_view(), name='MovieDetailView'),
	path('person-catalog/', PersonView.as_view(), name='PersonView'),


	path('filter/', MovieFilterView.as_view(), name='MovieFilterView'),
	path('search/', SearchManager.as_view(), name='SearchManager'),

	path('producer/<slug:slug>/', ProducerDetailView.as_view(), name='ProducerDetailView'),
	path('actor/<slug:slug>/', ActorDetailView.as_view(), name='ActorDetailView'),
]
