from django import forms

from .models import (Movie, Actor, Producer, 
	Rating, RatingStar, Review)


class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ('name', 'email', 'comment')


class RatingStarForm(forms.ModelForm):
	# Форма обработки звезд 
	star = forms.ModelChoiceField(queryset=RatingStar.objects.all(), 
		widget=forms.RadioSelect(), empty_label=None)

	class Meta:
		model = Rating 
		fields = ('star', )