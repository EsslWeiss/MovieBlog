from django.contrib import admin
from django.utils.html import mark_safe

from .models import Movie, MovieShot, Genre, Category
from .models import Actor, Producer
from django.contrib.sessions.models import Session

from .ckeditor_forms import (MovieCKEditorForm, ActorsCKEditorForm, ProducersCKEditorForm)

from modeltranslation.admin import TranslationAdmin


class MovieShotInlines(admin.TabularInline):
	model = MovieShot
	extra = 0 
	readonly_fields = ('get_image', 'get_background_image', 'get_additional_image')

	def get_image(self, obj): 
		return mark_safe(f'<img src={obj.image.url} width="100" heigth="100">')

	def get_background_image(self, obj):
		return mark_safe(f'<img src={obj.background_image.url} width="100" heigth="100">')

	def get_additional_image(self, obj):
		return mark_safe(f'<img src={obj.additional_image.url} width="100" heigth="100">')

	get_image.short_description = 'Image'
	get_background_image.short_description = 'Background image'
	get_additional_image.short_description = 'Additional image'


class GenreInlines(admin.TabularInline):
	model = Genre
	fields = ('name', 'url')
	extra = 0 


class MovieActorsInline(admin.TabularInline):
	model = Movie.actors.through
	verbose_name = 'Movie'
	verbose_name_plural = 'Movies'
	extra = 0


class MovieProducersInline(admin.TabularInline):
	model = Movie.producers.through  # Указание промежуточной модели Movie_producers.
	verbose_name = 'Movie'
	verbose_name_plural = 'Movies'
	extra = 0

@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
	list_display = ('title', 'tagline', 'description', 'get_producers', 'get_actors', 
		'get_genres', 'budget', 'world_premiere_date', 'url', 'draft')
	prepopulated_fields = {'url': ('title', )}
	list_display_links = ('title', )
	list_editable = ('tagline', 'draft')
	list_filter = ('genres', 'world_premiere_date', 'draft')
	search_fields = ('title', 'description', 'tagline')

	inlines = [MovieShotInlines, ]
	form = MovieCKEditorForm  # Добавление виджета CKEditor для модели Movie

	def get_producers(self, obj: Movie) -> str:
		return '\n'.join([f'{val.name} {val.surname}' for val in obj.producers.all()])

	def get_actors(self, obj: Movie) -> str:
		return '\n'.join([f'{val.name} {val.surname}' for val in obj.actors.all()])

	def get_genres(self, obj: Movie) -> str:
		return '\n'.join([val.name for val in obj.genres.all()])

	get_producers.short_description = 'Producers'
	get_actors.short_description = 'Actors'
	get_genres.short_description = 'Genres'


@admin.register(MovieShot)
class MovieShotAdmin(admin.ModelAdmin):
	list_display = ('title', 'get_image', 'get_background_image', 'get_additional_image')
	list_display_links = ('title', )

	def get_image(self, obj: MovieShot) -> mark_safe: 
		return mark_safe(f'<img src={obj.image.url} width="100" heigth="100">')

	def get_background_image(self, obj: MovieShot) -> mark_safe:
		return mark_safe(f'<img src={obj.background_image.url} width="100" heigth="100">')

	def get_additional_image(self, obj: MovieShot) -> mark_safe:
		return mark_safe(f'<img src={obj.additional_image.url} width="100" heigth="100">')

	get_image.short_description = 'Image'
	get_background_image.short_description = 'Background image'
	get_additional_image.short_description = 'Additional image'


@admin.register(Genre)
class GenreAdmin(TranslationAdmin):
	list_display = ('name', 'description', 'url')
	list_display_links = ('name', 'url')
	prepopulated_fields = {'url': ('name', )}


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
	list_display = ('name', 'description', 'url')
	list_display_links = ('name', 'url')
	prepopulated_fields = {'url': ('name', )}


@admin.register(Actor)
class ActorAdmin(TranslationAdmin):
	list_display = ('name', 'surname', 'gender', 'biography',
		'awards', 'get_image', 'get_icon', 'url')
	list_display_links = ('name', 'surname')
	list_filter = ('gender', )
	prepopulated_fields = {'url': ('name', 'surname')}
	inlines = [MovieActorsInline, ]
	form = ActorsCKEditorForm

	def get_image(self, obj: Actor) -> mark_safe:
		return mark_safe(f'<img src={obj.image.url} width="150" heigth="150">')

	def get_icon(self, obj: Actor) -> mark_safe:
		return mark_safe(f'<img src={obj.icon.url} width="50" heigth="50">') 

	get_image.short_description = 'Image'
	get_icon.short_description = 'Icon'


@admin.register(Producer)
class ProducerAdmin(TranslationAdmin):
	list_display = ('name', 'surname', 'gender', 'biography',
		'awards', 'get_image', 'get_icon', 'url')
	list_display_links = ('name', 'surname')
	list_filter = ('gender', )
	prepopulated_fields = {'url': ('name', 'surname')}
	inlines = [MovieProducersInline, ]
	form = ProducersCKEditorForm

	def get_image(self, obj: Actor) -> mark_safe:
		return mark_safe(f'<img src={obj.image.url} width="150" heigth="150">')

	def get_icon(self, obj: Actor) -> mark_safe:
		return mark_safe(f'<img src={obj.icon.url} width="50" heigth="50">') 

	get_image.short_description = 'Image'
	get_icon.short_description = 'Icon'


admin.site.register(Session)

admin.site.site_title = 'Administration Site'
admin.site.site_header = 'Administration Site'
