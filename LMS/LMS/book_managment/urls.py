from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'languages', LanguagesViewSet)
router.register(r'authors', AuthorsViewSet)
router.register(r'publishers', PublishersViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'sections', SectionsViewSet)
router.register(r'faculties', FacultiesViewSet)
router.register(r'books', BooksViewSet)
router.register(r'eBooks', eBooksViewSet)
router.register(r'copies', CopiesViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
