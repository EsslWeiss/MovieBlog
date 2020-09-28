from django.shortcuts import render
from django.views.generic.base import View 
from django.views.generic import ListView, DetailView

from .forms import ReviewForm, RatingStarForm

from .models import Movie, Actor, Producer
from .mixins import GenreYearMixin

from itertools import chain
from django.db.models import Q


class MainPageView(ListView):
	template_name = 'MainApp/mainpage.html'
	queryset = Movie

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['movies'] = Movie.objects.filter(draft=False)[:3]
		context['recently_added_films'] = Movie.objects\
			.filter(draft=False).order_by('world_premiere_date')
		return context


class MovieView(GenreYearMixin, ListView): 
	# view.get_genre обращение к методу миксина из шаблона
	queryset = Movie.objects.filter(draft=False)
	context_object_name = 'movies'
	template_name = 'MainApp/moviecatalog.html'
	paginate_by = 1


class MovieDetailView(GenreYearMixin, DetailView):
	model = Movie
	slug_field = 'url'
	context_object_name = 'details'
	template_name = 'MainApp/moviedetailpage.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['rating_form'] = RatingStarForm().fields.get('star').choices
		return context


class SearchManager(GenreYearMixin, ListView):
	context_object_name = 'movies'
	template_name = 'MainApp/moviecatalog.html'
	paginate_by = 1

	def get_queryset(self):
		return Movie.objects.filter(title__icontains=self.request.GET.get('search'))

	def get_context_data(self, **kwargs): 
		context = super().get_context_data(*args, **kwargs)
		context['search'] = f'search={self.request.GET.get("search")}&'
		return context


class PersonView(ListView):
	context_object_name = 'person'
	queryset = Movie.objects.all()
	template_name = 'MainApp/personcatalog.html'

	def person_chain(self):
		actors = Actor.objects.all()
		producers = Producer.objects.all()
		person_list = sorted(
				chain(actors, producers),
				key=lambda person: person.age, 
				reverse=True
			)
		return person_list

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['persons'] = self.person_chain()
		return context


class MovieFilterView(GenreYearMixin, ListView):
	context_object_name = 'movies'
	template_name = 'MainApp/moviecatalog.html'
	paginate_by = 1

	def get_queryset(self):
		queryset = Movie.objects.filter(
			(
				Q(world_premiere_date__year__in=self.request.GET.getlist('year')) |
				Q(genres__pk__in=self.request.GET.getlist('genre')) |
				Q(category_pk_in=self.request.GET.getlist('category'))
			) & Q(draft=False)
		).distinct()
		return queryset

	def filter_get_param(self, param):
		# возвращаемая строка: year=2020&category=test1&genre=test2&
		return ''.join(
			[f'{param}={val}&' for val in self.request.GET.getlist(f'{param}')]
			)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['year'] = self.filter_get_param('year')
		context['category'] = self.filter_get_param('category')
		context['genre'] = self.filter_get_param('genre')
		return context
