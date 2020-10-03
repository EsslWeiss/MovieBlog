from django.db import models
from django.urls import reverse


class AbsPerson(models.Model):
	GENDER_CHOICE = [
		('MALE', 'male'),
		('FEMALE', 'female')
	]

	name = models.CharField(max_length=60)
	surname = models.CharField(max_length=60)
	gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
	biography = models.TextField()
	awards = models.TextField()
	image = models.ImageField(upload_to='%(class)s_image')
	icon = models.ImageField(upload_to='%(class)s_icon')
	url = models.SlugField(unique=True)

	class Meta:
		abstract=True


class Actor(AbsPerson):
	def get_absolute_url(self):
		return reverse('ProducerDetailView', kwargs={'slug': self.url})

	def __str__(self):
		return f'{self.name} {self.surname}'

	class Meta:
		verbose_name='Actor'
		verbose_name_plural='Actors'


class Producer(AbsPerson):
	def get_absolute_url(self):
		return reverse('ActorDetailView', kwargs={'slug': self.url})

	def __str__(self):
		return f'{self.name} {self.surname}'

	class Meta:
		verbose_name='Producer'
		verbose_name_plural='Producers'	
