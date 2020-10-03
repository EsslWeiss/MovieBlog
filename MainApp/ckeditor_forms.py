from django import forms

from .models import Movie, Actor

from ckeditor.widgets import CKEditorWidget


class MovieCKEditorForm(forms.ModelForm):
	# Добавление в поле описания виджета CKEditor
	description_ru = forms.CharField(label='description', widget=CKEditorWidget())
	description_eng = forms.CharField(label='description', widget=CKEditorWidget())

	class Meta:
		model = Movie
		fields = '__all__'


class ActorsCKEditorForm(forms.ModelForm):
	# Добавление в поле биографии и наград виджета CKEditor
	biography_ru = forms.CharField(widget=CKEditorWidget())
	biography_eng = forms.CharField(widget=CKEditorWidget()) 

	awards_ru = forms.CharField(widget=CKEditorWidget()) 
	awards_eng = forms.CharField(widget=CKEditorWidget()) 

	class Meta:
		model = Actor
		fields = '__all__'


class ProducersCKEditorForm(forms.ModelForm):
	# Добавление в поле биографии и наград виджета CKEditor
	biography_ru = forms.CharField(widget=CKEditorWidget()) 
	biography_eng = forms.CharField(widget=CKEditorWidget()) 

	awards_ru = forms.CharField(widget=CKEditorWidget()) 
	awards_eng = forms.CharField(widget=CKEditorWidget()) 

	class Meta:
		model = Actor
		fields = '__all__'
