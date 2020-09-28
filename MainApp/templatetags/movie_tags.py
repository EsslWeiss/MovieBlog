from django.template.loader import get_template

from django import template
from MainApp.models import Category, Movie


register = template.Library()

@register.simple_tag
def categories_list():
	return Category.objects.all()

@register.inclusion_tag('MainApp/tags/recently_added.html')
def recently_added_movie(count=4):
	movies = Movie.objects.order_by('-world_premiere_date')[:count]
	return {'recently_added': movies}
