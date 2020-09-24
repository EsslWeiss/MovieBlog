from django.db import models
from django.urls import reverse
from .persons import Producer, Actor


class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	url = models.SlugField(unique=True, max_length=100)

	def get_absolute_url(self):
		return reverse('')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Category'
		verbose_name_plural='Categories'


class Genre(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, 
		related_name='genres', related_query_name='genres_query')
	url = models.SlugField(max_length=100, unique=True)

	def get_absolute_url(self):
		return reverse('')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Genre'
		verbose_name_plural='Genres'


class Country(models.Model):
	COUNTRY_CHOICE = [
		('USA', 'USA'),
		('FRA', 'France'), 
		('GER', 'Germany'),
		('RUS', 'Russia')
	]

	name = models.CharField(max_length=20, choices=COUNTRY_CHOICE)
	date_premiere = models.DateField()
	box_office = models.PositiveIntegerField(default=0)


class Movie(models.Model):
	title = models.CharField(max_length=100)
	tagline = models.CharField(max_length=100, default='')
	description = models.TextField()

	producers = models.ManyToManyField(Producer, 
		related_name='movies', related_query_name='movies_query')
	actors = models.ManyToManyField(Actor, 
		related_name='movies', related_query_name='movies_query')

	genres = models.ManyToManyField(Genre, 
		related_name='movies', related_query_name='movies_query')
	budget = models.PositiveIntegerField()
	world_premiere_date = models.DateField()
	country_premiere = models.ManyToManyField(Country, 
		related_name='movies', related_query_name='movies_query')
	url = models.SlugField(max_length=120, unique=True)
	draft = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse('')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Movie'
		verbose_name_plural='Movies'


class MovieShot(models.Model):
	title = models.CharField(max_length=20)
	description = models.TextField()
	image = models.ImageField(upload_to='movie_shots/')
	film = models.ForeignKey(Movie, on_delete=models.CASCADE, 
		related_name='movie_shots', related_query_name='movie_shots_query')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name='Movie shot'
		verbose_name_plural='Movie shots'