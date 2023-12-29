from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class LanguagesViewSet(viewsets.ModelViewSet):
    serializer_class = LanguagesSerializer
    queryset = Languages.objects.all()


class AuthorsViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorsSerializer
    queryset = Authors.objects.all()


class PublishersViewSet(viewsets.ModelViewSet):
    serializer_class = PublishersSerializer
    queryset = Publishers.objects.all()


class CategoriesViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Categories.objects.all()


class SectionsViewSet(viewsets.ModelViewSet):
    serializer_class = SectionsSerializer
    queryset = Sections.objects.all()


class FacultiesViewSet(viewsets.ModelViewSet):
    serializer_class = FacultiesSerializer
    queryset = Faculties.objects.all()


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()


class eBooksViewSet(viewsets.ModelViewSet):
    serializer_class = eBooksSerializer
    queryset = eBooks.objects.all()


class CopiesViewSet(viewsets.ModelViewSet):
    serializer_class = CopiesSerializer
    queryset = Copies.objects.all()


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()