from django.shortcuts import render

from django.views.generic.base import View 

# from .models.movies import Movie
from .models import Movie


class MainView(View):
	template_name = 'MainApp/mainpage.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['movies'] = Movie.objects.filter(draft=False)[:3]
		return context

