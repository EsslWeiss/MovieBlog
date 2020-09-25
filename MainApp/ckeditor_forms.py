from django import forms

from .models import Movie, Actor

from ckeditor.widgets import CKEditorWidget


class MovieCKEditorForm(forms.ModelForm):
	# Добавление в поле описания виджета CKEditor
	description = forms.CharField(widget=CKEditorWidget())

	class Meta:
		model = Movie
		fields = '__all__'


class ActorsCKEditorForm(forms.ModelForm):
	# Добавление в поле биографии и наград виджета CKEditor
	biography = forms.CharField(widget=CKEditorWidget()) 
	awards = forms.CharField(widget=CKEditorWidget()) 

	class Meta:
		model = Actor
		fields = '__all__'


class ProducersCKEditorForm(forms.ModelForm):
	# Добавление в поле биографии и наград виджета CKEditor
	biography = forms.CharField(widget=CKEditorWidget()) 
	awards = forms.CharField(widget=CKEditorWidget()) 

	class Meta:
		model = Actor
		fields = '__all__'
