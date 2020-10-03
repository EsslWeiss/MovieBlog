from django.db import models
from django.urls import reverse

from .movies import Movie


class RatingStar(models.Model):
	value = models.SmallIntegerField(default=0)

	def __str__(self):
		return self.value

	class Meta:
		verbose_name='rating star'
		verbose_name_plural='rating stars'
		ordering = ['-value']


class Rating(models.Model): 
	ip = models.CharField('ip-address', max_length=15)
	star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.movie} - {self.star}'

	class Meta:
		verbose_name='rating'
		verbose_name_plural='ratings'


class Review(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE, 
		related_name='review', related_query_name='review_query')
	name = models.CharField(max_length=100)
	comment = models.TextField()
	email = models.EmailField()
	parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL,
		related_name='parent_review', null=True, blank=True)
	date_created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.name}: {self.comments}'

	class Meta:
		verbose_name='review'
		verbose_name_plural='reviews'
		ordering = ['-date_created']
