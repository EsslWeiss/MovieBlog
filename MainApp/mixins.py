from .models import (Genre, Category, Movie, Actor, Producer)


class GenreYearMixin:
	def get_genres(self):
		return Genre.objects.all()

	def get_categories(self):
		return Category.objects.all()

	def get_years(self):
		return Movie.objects.filter(draft=False)\
			.values('world_premiere_date__year')\
			.distinct()


class ActorProducersMixin:
	def get_actors(self):
		return Actor.objects.all()

	def get_producers(self):
		return Producer.objects.all()
