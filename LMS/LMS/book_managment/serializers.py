from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import (Languages, Authors,
                     Publishers, Categories, Sections,
                     Faculties, Books, eBooks, Copies, News)


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class PublishersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishers
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = 'all'


class SectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sections
        fields = 'all'


class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = 'all'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = 'all'


class eBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = eBooks
        fields = 'all'


class CopiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Copies
        fields = 'all'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'all'
