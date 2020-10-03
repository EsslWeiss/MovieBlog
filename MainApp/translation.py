from modeltranslation.translator import register, TranslationOptions

from .models import Actor, Producer, Category, Genre, Movie


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
	fields = ('title', 'tagline', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
	fields = ('name', 'description')


@register(Genre)
class GenreTranslationOptions(TranslationOptions):
	fields = ('name', 'description')


@register(Actor)
class ActorTranslationOptions(TranslationOptions):
	fields = ('name', 'surname', 'gender', 'biography', 'awards')


@register(Producer)
class ProducerTranslationOptions(TranslationOptions):
	fields = ('name', 'surname', 'gender', 'biography', 'awards')
